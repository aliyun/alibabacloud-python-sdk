# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AcceptApproveCommandRequest(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.command_id = command_id
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AcceptApproveCommandResponseBody(TeaModel):
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


class AcceptApproveCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AcceptApproveCommandResponseBody = None,
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
            temp_model = AcceptApproveCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AcceptOperationTicketRequest(TeaModel):
    def __init__(
        self,
        effect_count: str = None,
        effect_end_time: str = None,
        effect_start_time: str = None,
        instance_id: str = None,
        operation_ticket_id: str = None,
        region_id: str = None,
    ):
        # The maximum number of logons allowed. Valid values:
        # 
        # *   0: The number of logons is unlimited. The O\&M engineer can log on to the specified asset for an unlimited number of times during the validity period.
        # *   1: The O\&M engineer can log on to the specified asset only once during the validity period.
        # 
        # >  You can set this parameter only to 0 if you review an O\&M application on a database.
        self.effect_count = effect_count
        # The end time of the validity period. The value is a UNIX timestamp. Unit: seconds.
        self.effect_end_time = effect_end_time
        # The start time of the validity period. The value is a UNIX timestamp. Unit: seconds.
        self.effect_start_time = effect_start_time
        # The ID of the bastion host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The ID of the O\&M application that you want to approve. You can call the ListOperationTickets operation to query the IDs of all O\&M applications that require review.
        self.operation_ticket_id = operation_ticket_id
        # The region ID of the bastion host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect_count is not None:
            result['EffectCount'] = self.effect_count
        if self.effect_end_time is not None:
            result['EffectEndTime'] = self.effect_end_time
        if self.effect_start_time is not None:
            result['EffectStartTime'] = self.effect_start_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.operation_ticket_id is not None:
            result['OperationTicketId'] = self.operation_ticket_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectCount') is not None:
            self.effect_count = m.get('EffectCount')
        if m.get('EffectEndTime') is not None:
            self.effect_end_time = m.get('EffectEndTime')
        if m.get('EffectStartTime') is not None:
            self.effect_start_time = m.get('EffectStartTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OperationTicketId') is not None:
            self.operation_ticket_id = m.get('OperationTicketId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AcceptOperationTicketResponseBody(TeaModel):
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


class AcceptOperationTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AcceptOperationTicketResponseBody = None,
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
            temp_model = AcceptOperationTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddHostsToGroupRequest(TeaModel):
    def __init__(
        self,
        host_group_id: str = None,
        host_ids: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the host group to which you want to add hosts.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_id = host_group_id
        # The ID of the host that you want to add to the host group. The value is a JSON string. You can add up to 100 host IDs.
        # 
        # > You can call the [ListHosts](~~200665~~) operation to query the IDs of hosts.
        self.host_ids = host_ids
        # The ID of the bastion host for which you want to add hosts to the host group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host for which you want to add hosts to the host group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddHostsToGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_group_id: str = None,
        host_id: str = None,
        message: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # 
        # *   **UNEXPECTED**: An unknown error occurred.
        # 
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # 
        # >Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        # >Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The ID of the host group.
        self.host_group_id = host_group_id
        # The ID of the host.
        self.host_id = host_id
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddHostsToGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AddHostsToGroupResponseBodyResults] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: AddHostsToGroupResponseBody = None,
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
            temp_model = AddHostsToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUsersToGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
        user_ids: str = None,
    ):
        # The ID of the bastion host for which you want to add users to the user group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host for which you want to add users to the user group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user group to which you want to add users.
        # 
        # > You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id
        # The ID of the user that you want to add to the user group. The value is a JSON string. You can add up to 100 user IDs. If you specify multiple IDs, separate the IDs with commas (,).
        # 
        # > You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        code: str = None,
        message: str = None,
        user_group_id: str = None,
        user_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # 
        # *   **UNEXPECTED**: An unknown error occurred.
        # 
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # 
        #     **\
        # 
        #     **Note**Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        #     **\
        # 
        #     **Note**Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # This parameter is deprecated.
        self.message = message
        # The ID of the group.
        self.user_group_id = user_group_id
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddUsersToGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AddUsersToGroupResponseBodyResults] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: AddUsersToGroupResponseBody = None,
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
            temp_model = AddUsersToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostAccountsToHostShareKeyRequest(TeaModel):
    def __init__(
        self,
        host_account_ids: str = None,
        host_share_key_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The IDs of the host accounts.
        # 
        # > You must specify this parameter.
        self.host_account_ids = host_account_ids
        # The ID of the shared key.
        # 
        # > You must specify this parameter.
        self.host_share_key_id = host_share_key_id
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_ids is not None:
            result['HostAccountIds'] = self.host_account_ids
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountIds') is not None:
            self.host_account_ids = m.get('HostAccountIds')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AttachHostAccountsToHostShareKeyResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_id: str = None,
        host_share_key_id: str = None,
        message: str = None,
    ):
        # The error code returned. If **OK** is returned, the association was successful. If another error code is returned, the association failed.
        self.code = code
        # The ID of the host account.
        self.host_account_id = host_account_id
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The error message returned.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachHostAccountsToHostShareKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AttachHostAccountsToHostShareKeyResponseBodyResults] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = AttachHostAccountsToHostShareKeyResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AttachHostAccountsToHostShareKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachHostAccountsToHostShareKeyResponseBody = None,
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
            temp_model = AttachHostAccountsToHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostAccountsToUserRequest(TeaModel):
    def __init__(
        self,
        hosts: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The IDs of the host and host account that you want to authorize the user to manage. You can specify up to 10 host IDs and up to 10 host account IDs for each host. You can specify only host IDs. In this case, the user is authorized to manage only the specified hosts. For more information about this parameter, see the "Description of the Hosts parameter" section of this topic.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host and the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.hosts = hosts
        # The ID of the bastion host for which you want to authorize the user to manage the specified hosts and host accounts.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host for which you want to authorize the user to manage the specified hosts and host accounts.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user that you want to authorize to manage the specified hosts and host accounts.
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AttachHostAccountsToUserResponseBodyResultsHostAccounts(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_id: str = None,
        message: str = None,
    ):
        # The return code that indicates whether the user was authorized to manage the specified host account. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The ID of the host account.
        self.host_account_id = host_account_id
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachHostAccountsToUserResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_accounts: List[AttachHostAccountsToUserResponseBodyResultsHostAccounts] = None,
        host_id: str = None,
        message: str = None,
        user_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # 
        # *   **UNEXPECTED**: An unknown error occurred.
        # 
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # 
        # > Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        # > Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The result of authorizing the specified user to manage the specified host accounts.
        self.host_accounts = host_accounts
        # The ID of the host.
        self.host_id = host_id
        # This parameter is deprecated.
        self.message = message
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = AttachHostAccountsToUserResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AttachHostAccountsToUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AttachHostAccountsToUserResponseBodyResults] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: AttachHostAccountsToUserResponseBody = None,
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
            temp_model = AttachHostAccountsToUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostAccountsToUserGroupRequest(TeaModel):
    def __init__(
        self,
        hosts: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The IDs of the host and host account that you want to authorize the user group to manage. You can specify up to 10 host IDs and up to 10 host account IDs for each host. You can specify only host IDs. In this case, the user group is authorized to manage only the specified hosts. For more information about this parameter, see the "Description of the Hosts parameter" section of this topic.
        # 
        # > You can call the [ListHosts](~~200665~~) operation to query the ID of the host and the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.hosts = hosts
        # The ID of the bastion host in which you want to authorize the user group to manage the specified hosts and host accounts.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host in which you want to authorize the user group to manage the specified hosts and host accounts.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user group that you want to authorize to manage the specified hosts and host accounts.
        # 
        # > You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AttachHostAccountsToUserGroupResponseBodyResultsHostAccounts(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_id: str = None,
        message: str = None,
    ):
        # The return code that indicates whether the user group was authorized to manage the specified host account. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The ID of the host account.
        self.host_account_id = host_account_id
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachHostAccountsToUserGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_accounts: List[AttachHostAccountsToUserGroupResponseBodyResultsHostAccounts] = None,
        host_id: str = None,
        message: str = None,
        user_group_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The result of authorizing the specified user group to manage the specified host accounts.
        self.host_accounts = host_accounts
        # The ID of the host.
        self.host_id = host_id
        # This parameter is deprecated.
        self.message = message
        # The ID of the user group.
        self.user_group_id = user_group_id

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = AttachHostAccountsToUserGroupResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AttachHostAccountsToUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AttachHostAccountsToUserGroupResponseBodyResults] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: AttachHostAccountsToUserGroupResponseBody = None,
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
            temp_model = AttachHostAccountsToUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostGroupAccountsToUserRequest(TeaModel):
    def __init__(
        self,
        host_groups: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The ID of the host group and the name of the host account that you want to authorize the user to manage. You can specify up to 10 host group IDs and up to 10 host account names for each host group. You can specify only host group IDs. In this case, the user is authorized to manage only the specified host groups. For more information about this parameter, see the "Description of the HostGroups parameter" section of this topic.
        # 
        # >  You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group and the [ListHostAccounts](~~204372~~) operation to query the name of the host account.
        self.host_groups = host_groups
        # The ID of the bastion host for which you want to authorize the user to manage the specified host groups and host accounts.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host for which you want to authorize the user to manage the specified host groups and host accounts.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user that you want to authorize to manage the specified host groups and host accounts.
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_name: str = None,
        message: str = None,
    ):
        # The return code that indicates whether the user was authorized to manage the specified host account. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The name of the host account.
        self.host_account_name = host_account_name
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachHostGroupAccountsToUserResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_names: List[AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames] = None,
        host_group_id: str = None,
        message: str = None,
        user_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The result of authorizing the user to manage the specified host accounts.
        self.host_account_names = host_account_names
        # The ID of the host group.
        self.host_group_id = host_group_id
        # This parameter is deprecated.
        self.message = message
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        if self.host_account_names:
            for k in self.host_account_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k in self.host_account_names:
                result['HostAccountNames'].append(k.to_map() if k else None)
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k in m.get('HostAccountNames'):
                temp_model = AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k))
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AttachHostGroupAccountsToUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AttachHostGroupAccountsToUserResponseBodyResults] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: AttachHostGroupAccountsToUserResponseBody = None,
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
            temp_model = AttachHostGroupAccountsToUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostGroupAccountsToUserGroupRequest(TeaModel):
    def __init__(
        self,
        host_groups: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The ID of the host group and the name of the host account that you want to authorize the user group to manage. You can specify up to 10 host group IDs and up to 10 host account names for each host group. You can specify only host group IDs. In this case, the user group is authorized to manage only the specified host groups. For more information about this parameter, see the "Description of the HostGroups parameter" section of this topic.
        # 
        # >  You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group and the [ListHostAccounts](~~204372~~) operation to query the name of the host account.
        self.host_groups = host_groups
        # The ID of the bastion host for which you want to authorize the user group to manage the specified host groups and host accounts.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host for which you want to authorize the user group to manage the specified host groups and host accounts.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user group that you want to authorize to manage the specified host groups and host accounts.
        # 
        # >  You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AttachHostGroupAccountsToUserGroupResponseBodyResultsHostAccountNames(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_name: str = None,
        message: str = None,
    ):
        # The return code that indicates whether the user group was authorized to manage the specified host account. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The name of the host account.
        self.host_account_name = host_account_name
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachHostGroupAccountsToUserGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_names: List[AttachHostGroupAccountsToUserGroupResponseBodyResultsHostAccountNames] = None,
        host_group_id: str = None,
        message: str = None,
        user_group_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The result of authorizing the user group to manage the specified host accounts.
        self.host_account_names = host_account_names
        # The ID of the host group.
        self.host_group_id = host_group_id
        # This parameter is deprecated.
        self.message = message
        # The ID of the group.
        self.user_group_id = user_group_id

    def validate(self):
        if self.host_account_names:
            for k in self.host_account_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k in self.host_account_names:
                result['HostAccountNames'].append(k.to_map() if k else None)
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k in m.get('HostAccountNames'):
                temp_model = AttachHostGroupAccountsToUserGroupResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k))
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AttachHostGroupAccountsToUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AttachHostGroupAccountsToUserGroupResponseBodyResults] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: AttachHostGroupAccountsToUserGroupResponseBody = None,
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
            temp_model = AttachHostGroupAccountsToUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceSecurityGroupsRequest(TeaModel):
    def __init__(
        self,
        authorized_security_groups: List[str] = None,
        instance_id: str = None,
        lang: str = None,
        region_id: str = None,
    ):
        # An array that consists of the IDs of authorized security groups.
        self.authorized_security_groups = authorized_security_groups
        # The ID of the bastion host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The region ID of the bastion host.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_security_groups is not None:
            result['AuthorizedSecurityGroups'] = self.authorized_security_groups
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedSecurityGroups') is not None:
            self.authorized_security_groups = m.get('AuthorizedSecurityGroups')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigInstanceSecurityGroupsResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # The ID of the bastion host for which security groups were configured.
        self.instance_id = instance_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigInstanceSecurityGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigInstanceSecurityGroupsResponseBody = None,
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
            temp_model = ConfigInstanceSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceWhiteListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        white_list: List[str] = None,
    ):
        # The ID of the bastion host for which a whitelist of public IP addresses is configured.
        self.instance_id = instance_id
        # Configures a whitelist of public IP addresses for a bastion host.
        self.region_id = region_id
        # ConfigInstanceWhiteList
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        instance_id: str = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigInstanceWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigInstanceWhiteListResponseBody = None,
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
            temp_model = ConfigInstanceWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostRequest(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        host_name: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        instance_id: str = None,
        instance_region_id: str = None,
        network_domain_id: str = None,
        ostype: str = None,
        region_id: str = None,
        source: str = None,
        source_instance_id: str = None,
    ):
        # The endpoint type of the host that you want to create. Valid values:
        # 
        # *   **Public**: public endpoint
        # *   **Private**: internal endpoint
        self.active_address_type = active_address_type
        # The description of the host that you want to create. The value can be up to 500 characters in length.
        self.comment = comment
        # The name of the host that you want to create. The name can be up to 128 characters in length.
        self.host_name = host_name
        # The internal endpoint of the host that you want to create. You can set this parameter to a domain name or an IP address.
        # 
        # > This parameter is required if the **ActiveAddressType** parameter is set to **Private**.
        self.host_private_address = host_private_address
        # The public endpoint of the host that you want to create. You can set this parameter to a domain name or an IP address.
        # 
        # > This parameter is required if the **ActiveAddressType** parameter is set to **Public**.
        self.host_public_address = host_public_address
        # The ID of the bastion host in which you want to create the host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The ID of the region to which the ECS instance or the host in an ApsaraDB MyBase dedicated cluster belongs.
        # 
        # > This parameter is required if the **Source** parameter is set to **Ecs** or **Rds**.
        self.instance_region_id = instance_region_id
        # The ID of the network domain to which the host belongs.
        self.network_domain_id = network_domain_id
        # The operating system of the host that you want to create. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.ostype = ostype
        # The region ID of the bastion host in which you want to create the host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The source of the host that you want to create. Valid values:
        # 
        # *   **Local**: a host in a data center
        # *   **Ecs**: an Elastic Compute Service (ECS) instance
        # *   **Rds**: a host in an ApsaraDB MyBase dedicated cluster
        self.source = source
        # The ID of the ECS instance or the host in an ApsaraDB MyBase dedicated cluster.
        # 
        # > This parameter is required if the **Source** parameter is set to **Ecs** or **Rds**.
        self.source_instance_id = source_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        return self


class CreateHostResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        # The ID of the host.
        self.host_id = host_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHostResponseBody = None,
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
            temp_model = CreateHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostAccountRequest(TeaModel):
    def __init__(
        self,
        host_account_name: str = None,
        host_id: str = None,
        host_share_key_id: str = None,
        instance_id: str = None,
        pass_phrase: str = None,
        password: str = None,
        private_key: str = None,
        protocol_name: str = None,
        region_id: str = None,
    ):
        # The passphrase of the private key for the host account.
        # 
        # >  You can specify this parameter when the ProtocolName parameter is set to SSH. If the ProtocolName parameter is set to RDP, you do not need to specify this parameter.
        self.host_account_name = host_account_name
        # The ID of the shared key.
        self.host_id = host_id
        # The protocol of the host to which you want to add a host account.
        # 
        # Valid values:
        # 
        # *   SSH
        # *   RDP
        self.host_share_key_id = host_share_key_id
        # master
        self.instance_id = instance_id
        # The private key of the host account. The value is a Base64-encoded string.
        # 
        # >  This parameter takes effect only when the ProtocolName parameter is set to SSH. If the ProtocolName parameter is set to RDP, you do not need to specify this parameter. You can configure a password and a private key for the host account at the same time. If both a password and a private key are configured for the host account, Bastionhost preferentially uses the private key to log on to the host.
        self.pass_phrase = pass_phrase
        # The region ID of the bastion host in which you want to add a host account to the host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.password = password
        # The ID of the host to which you want to add a host account.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.private_key = private_key
        # The ID of the bastion host in which you want to add a host account to the host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.protocol_name = protocol_name
        # The password of the host account.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase
        if self.password is not None:
            result['Password'] = self.password
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        host_account_id: str = None,
        request_id: str = None,
    ):
        # The ID of the request.
        self.host_account_id = host_account_id
        # The operation that you want to perform. Set the value to **CreateHostAccount**.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHostAccountResponseBody = None,
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
            temp_model = CreateHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostGroupRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        host_group_name: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The description of the host group. The description can be up to 500 characters in length.
        self.comment = comment
        # The name of the host group. The name can be up to 128 characters in length.
        self.host_group_name = host_group_name
        # The ID of the bastion host on which you want to create a host group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host on which you want to create a host group.
        # 
        # **\
        # 
        # **For more information about the mapping between region IDs and region names, see **Regions and zones[.](~~40654~~)
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        host_group_id: str = None,
        request_id: str = None,
    ):
        # The ID of the host group.
        self.host_group_id = host_group_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateHostGroupResponseBody = None,
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
            temp_model = CreateHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostShareKeyRequest(TeaModel):
    def __init__(
        self,
        host_share_key_name: str = None,
        instance_id: str = None,
        pass_phrase: str = None,
        private_key: str = None,
        region_id: str = None,
    ):
        # The name of the shared key that you want to create. The name can be a maximum of 128 characters in length.
        self.host_share_key_name = host_share_key_name
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The password of the private key. The value is a Base64-encoded string.
        self.pass_phrase = pass_phrase
        # The private key. The value is a Base64-encoded string.
        self.private_key = private_key
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateHostShareKeyResponseBody(TeaModel):
    def __init__(
        self,
        host_share_key_id: int = None,
        request_id: str = None,
    ):
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateHostShareKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHostShareKeyResponseBody = None,
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
            temp_model = CreateHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        display_name: str = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        email: str = None,
        instance_id: str = None,
        language: str = None,
        language_status: str = None,
        mobile: str = None,
        mobile_country_code: str = None,
        need_reset_password: bool = None,
        password: str = None,
        region_id: str = None,
        source: str = None,
        source_user_id: str = None,
        two_factor_methods: str = None,
        two_factor_status: str = None,
        user_name: str = None,
    ):
        # The remarks of the user that you want to add. The remarks can be up to 500 characters in length.
        self.comment = comment
        # The display name of the user that you want to add. This display name can be up to 128 characters in length.
        self.display_name = display_name
        # The end of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time
        # The beginning of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time
        # The email address of the user that you want to add.
        self.email = email
        # The ID of the bastion host to which you want to add a user.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        self.language = language
        self.language_status = language_status
        # The mobile phone number of the user that you want to add.
        self.mobile = mobile
        # The country where the mobile number of the user is registered. Default value: **CN**. Valid values:
        # 
        # *   **CN**: the Chinese mainland, whose country calling code is +86
        # *   **HK**: Hong Kong (China), whose country calling code is +852
        # *   **MO**: Macau (China), whose country calling code is +853
        # *   **TW**: Taiwan (China), whose country calling code is +886
        # *   **RU**: Russia, whose country calling code is +7
        # *   **SG**: Singapore, whose country calling code is +65
        # *   **MY**: Malaysia, whose country calling code is +60
        # *   **ID**: Indonesia, whose country calling code is +62
        # *   **DE**: Germany, whose country calling code is +49
        # *   **AU**: Australia, whose country calling code is +61
        # *   **US**: US, whose country calling code is +1
        # *   **AE**: United Arab Emirates, whose country calling code is +971
        # *   **JP**: Japan, whose country calling code is +81
        # *   **GB**: UK, whose country calling code is +44
        # *   **IN**: India, whose country calling code is +91
        # *   **KR**: Republic of Korea, whose country calling code is +82
        # *   **PH**: Philippines, whose country calling code is +63
        # *   **CH**: Switzerland, whose country calling code is +41
        # *   **SE**: Sweden, whose country calling code is +46
        self.mobile_country_code = mobile_country_code
        # Specifies whether password reset is required upon the next logon. Valid values:
        # 
        # - true: yes
        # 
        # - false: no
        self.need_reset_password = need_reset_password
        # The logon password of the user that you want to add. The logon password can be up to 128 characters in length.
        # 
        # >  This parameter is required if the **Source** parameter is set to **Local**.
        self.password = password
        # The region ID of the bastion host to which you want to add a user.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The source of the user that you want to add. Valid values:
        # 
        # - **Local**: a local user
        # - **Ram**: a RAM user
        # - **AD** : an AD-authenticated user
        # - **LDAP** : an LDAP-authenticated user
        self.source = source
        # The unique identifier of the user that you want to add.
        # 
        # >  This parameter uniquely identifies a RAM user of the bastion host. This parameter is required if the **Source** parameter is set to **Ram**. You can call the [ListUsers](~~28684~~) operation to obtain the unique identifier of the user from the **UserId** response parameter.
        self.source_user_id = source_user_id
        # The two-factor authentication method. You can select only one method. Valid values:
        # 
        # *   **sms:** text message
        # *   **email:** email
        # *   **dingtalk:** DingTalk
        # *   **totp OTP:** time-based one-time password (TOTP) app
        # 
        # > *   When the TwoFactorStatus parameter is set to Enable, you must specify one of the preceding values.
        self.two_factor_methods = two_factor_methods
        # The two-factor authentication status of the user. Valid values:
        # 
        # - Global: follows the global settings
        # - Disable: disables two-factor authentication
        # - Enable: enable two-factor authentication and follows settings of the single user
        self.two_factor_status = two_factor_status
        # The logon name of the user that you want to add. The logon name can contain only letters, digits, and underscores (\_) and can be up to 128 characters in length.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.email is not None:
            result['Email'] = self.email
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.language is not None:
            result['Language'] = self.language
        if self.language_status is not None:
            result['LanguageStatus'] = self.language_status
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.need_reset_password is not None:
            result['NeedResetPassword'] = self.need_reset_password
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        if self.two_factor_status is not None:
            result['TwoFactorStatus'] = self.two_factor_status
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageStatus') is not None:
            self.language_status = m.get('LanguageStatus')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('NeedResetPassword') is not None:
            self.need_reset_password = m.get('NeedResetPassword')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        if m.get('TwoFactorStatus') is not None:
            self.two_factor_status = m.get('TwoFactorStatus')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateUserResponseBody = None,
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
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserGroupRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_name: str = None,
    ):
        # The description of the user group. The description can be up to 500 characters in length.
        self.comment = comment
        # The ID of the bastion host for which you want to create a user group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host for which you want to create a user group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The name of the user group that you want to create. This name can be a up to 128 characters in length.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class CreateUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_group_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The ID of the user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateUserGroupResponseBody = None,
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
            temp_model = CreateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserPublicKeyRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        public_key: str = None,
        public_key_name: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The description of the public key. The description can be up to 500 characters in length.
        self.comment = comment
        # The ID of the bastion host on which you want to create a public key for the user.
        # 
        # > You can call the [listinstances](~~204522~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The public key. Encode the value by using the Base64 algorithm.
        self.public_key = public_key
        # The name of the public key.
        self.public_key_name = public_key_name
        # Specifies the region ID of the bastion host on which you want to create a public key for the user.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # Specifies the ID of the user for whom you want to create a public key.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.public_key_name is not None:
            result['PublicKeyName'] = self.public_key_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('PublicKeyName') is not None:
            self.public_key_name = m.get('PublicKeyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateUserPublicKeyResponseBody(TeaModel):
    def __init__(
        self,
        public_key_id: str = None,
        request_id: str = None,
    ):
        # The ID of the public key.
        self.public_key_id = public_key_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUserPublicKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserPublicKeyResponseBody = None,
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
            temp_model = CreateUserPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostRequest(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the host that you want to delete.
        # 
        # > You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.host_id = host_id
        # The ID of the bastion host on which you want to delete the host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host on which you want to delete the host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class DeleteHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHostResponseBody = None,
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
            temp_model = DeleteHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostAccountRequest(TeaModel):
    def __init__(
        self,
        host_account_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the host account that you want to remove.
        # 
        # >  You can call the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.host_account_id = host_account_id
        # The ID of the bastion host from which you want to remove the host account.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host from which you want to remove the host account.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class DeleteHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHostAccountResponseBody = None,
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
            temp_model = DeleteHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostGroupRequest(TeaModel):
    def __init__(
        self,
        host_group_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the host group that you want to delete.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_id = host_group_id
        # The ID of the bastion host from which you want to delete the host group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host from which you want to delete the host group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class DeleteHostGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHostGroupResponseBody = None,
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
            temp_model = DeleteHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostShareKeyRequest(TeaModel):
    def __init__(
        self,
        host_share_key_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the shared key.
        # 
        # > You must specify this parameter.
        self.host_share_key_id = host_share_key_id
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteHostShareKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class DeleteHostShareKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHostShareKeyResponseBody = None,
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
            temp_model = DeleteHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The ID of the bastion host to which the user to be deleted belongs.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host to which the user to be deleted belongs.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user to be deleted.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserResponseBody = None,
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
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The ID of the bastion host on which you want to delete the user group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host on which you want to delete the user group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user group that you want to delete.
        # 
        # > You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        # The ID of the request.
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


class DeleteUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserGroupResponseBody = None,
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
            temp_model = DeleteUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserPublicKeyRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        public_key_id: str = None,
        region_id: str = None,
    ):
        # The region ID of the bastion host on which you want to delete the public key from the user.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The ID of the public key.
        self.public_key_id = public_key_id
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteUserPublicKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class DeleteUserPublicKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserPublicKeyResponseBody = None,
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
            temp_model = DeleteUserPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceAttributeResponseBodyInstanceAttributePorts(TeaModel):
    def __init__(
        self,
        custom_port: int = None,
        standard_port: int = None,
    ):
        # The custom port.
        # 
        # >  You can change only the SSH and RDP ports. If O\&M ports are not specified, the value of the StandardPort parameter is returned.
        self.custom_port = custom_port
        # The standard port of the bastion host. Valid values:
        # 
        # *   **SSH**: 60022
        # *   **RDP**: 63389
        # *   **HTTPS**: 443
        self.standard_port = standard_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_port is not None:
            result['CustomPort'] = self.custom_port
        if self.standard_port is not None:
            result['StandardPort'] = self.standard_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPort') is not None:
            self.custom_port = m.get('CustomPort')
        if m.get('StandardPort') is not None:
            self.standard_port = m.get('StandardPort')
        return self


class DescribeInstanceAttributeResponseBodyInstanceAttribute(TeaModel):
    def __init__(
        self,
        authorized_security_groups: List[str] = None,
        bandwidth: str = None,
        bandwidth_package: str = None,
        db_operation_module: str = None,
        description: str = None,
        eni_instance_id: str = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_status: str = None,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        license_code: str = None,
        modify_password_module: str = None,
        network_proxy_module: str = None,
        ports: List[DescribeInstanceAttributeResponseBodyInstanceAttributePorts] = None,
        private_export_ips: List[str] = None,
        private_white_list: List[str] = None,
        public_export_ips: List[str] = None,
        public_ips: List[str] = None,
        public_network_access: bool = None,
        public_white_list: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_ids: List[str] = None,
        start_time: int = None,
        storage: int = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        web_terminal_module: str = None,
    ):
        self.authorized_security_groups = authorized_security_groups
        # The total bandwidth of the bastion host.
        self.bandwidth = bandwidth
        # The extra bandwidth plan of the bastion host.
        self.bandwidth_package = bandwidth_package
        self.db_operation_module = db_operation_module
        self.description = description
        self.eni_instance_id = eni_instance_id
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_status = instance_status
        self.internet_endpoint = internet_endpoint
        self.intranet_endpoint = intranet_endpoint
        self.license_code = license_code
        self.modify_password_module = modify_password_module
        self.network_proxy_module = network_proxy_module
        self.ports = ports
        self.private_export_ips = private_export_ips
        self.private_white_list = private_white_list
        self.public_export_ips = public_export_ips
        self.public_ips = public_ips
        self.public_network_access = public_network_access
        self.public_white_list = public_white_list
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.security_group_ids = security_group_ids
        self.start_time = start_time
        self.storage = storage
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.web_terminal_module = web_terminal_module

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_security_groups is not None:
            result['AuthorizedSecurityGroups'] = self.authorized_security_groups
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_package is not None:
            result['BandwidthPackage'] = self.bandwidth_package
        if self.db_operation_module is not None:
            result['DbOperationModule'] = self.db_operation_module
        if self.description is not None:
            result['Description'] = self.description
        if self.eni_instance_id is not None:
            result['EniInstanceId'] = self.eni_instance_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.modify_password_module is not None:
            result['ModifyPasswordModule'] = self.modify_password_module
        if self.network_proxy_module is not None:
            result['NetworkProxyModule'] = self.network_proxy_module
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.private_export_ips is not None:
            result['PrivateExportIps'] = self.private_export_ips
        if self.private_white_list is not None:
            result['PrivateWhiteList'] = self.private_white_list
        if self.public_export_ips is not None:
            result['PublicExportIps'] = self.public_export_ips
        if self.public_ips is not None:
            result['PublicIps'] = self.public_ips
        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access
        if self.public_white_list is not None:
            result['PublicWhiteList'] = self.public_white_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.web_terminal_module is not None:
            result['WebTerminalModule'] = self.web_terminal_module
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedSecurityGroups') is not None:
            self.authorized_security_groups = m.get('AuthorizedSecurityGroups')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthPackage') is not None:
            self.bandwidth_package = m.get('BandwidthPackage')
        if m.get('DbOperationModule') is not None:
            self.db_operation_module = m.get('DbOperationModule')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EniInstanceId') is not None:
            self.eni_instance_id = m.get('EniInstanceId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('ModifyPasswordModule') is not None:
            self.modify_password_module = m.get('ModifyPasswordModule')
        if m.get('NetworkProxyModule') is not None:
            self.network_proxy_module = m.get('NetworkProxyModule')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = DescribeInstanceAttributeResponseBodyInstanceAttributePorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('PrivateExportIps') is not None:
            self.private_export_ips = m.get('PrivateExportIps')
        if m.get('PrivateWhiteList') is not None:
            self.private_white_list = m.get('PrivateWhiteList')
        if m.get('PublicExportIps') is not None:
            self.public_export_ips = m.get('PublicExportIps')
        if m.get('PublicIps') is not None:
            self.public_ips = m.get('PublicIps')
        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')
        if m.get('PublicWhiteList') is not None:
            self.public_white_list = m.get('PublicWhiteList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('WebTerminalModule') is not None:
            self.web_terminal_module = m.get('WebTerminalModule')
        return self


class DescribeInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        instance_attribute: DescribeInstanceAttributeResponseBodyInstanceAttribute = None,
        request_id: str = None,
    ):
        # The attribute information about the bastion host.
        self.instance_attribute = instance_attribute
        self.request_id = request_id

    def validate(self):
        if self.instance_attribute:
            self.instance_attribute.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_attribute is not None:
            result['InstanceAttribute'] = self.instance_attribute.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceAttribute') is not None:
            temp_model = DescribeInstanceAttributeResponseBodyInstanceAttribute()
            self.instance_attribute = temp_model.from_map(m['InstanceAttribute'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceAttributeResponseBody = None,
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
            temp_model = DescribeInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        instance_status: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[DescribeInstancesRequestTag] = None,
    ):
        # An array that consists of the IDs of the bastion hosts.
        self.instance_id = instance_id
        # The status of the bastion host. Valid values:
        # 
        # *   **PENDING**: The bastion host is not initialized.
        # *   **CREATING**: The bastion host is being created.
        # *   **RUNNING**: The bastion host is running.
        # *   **EXPIRED**: The bastion host expired.
        # *   **CREATE_FAILED**: The bastion host fails to be created.
        # *   **UPGRADING**: The configurations of the bastion host are being changed.
        # *   **UPGRADE_FAILED**: The configurations of the bastion host fail to be changed.
        self.instance_status = instance_status
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The region ID of the bastion host.
        self.region_id = region_id
        # The ID of the resource group to which the bastion host belongs.
        self.resource_group_id = resource_group_id
        # An array consisting of the tags that are added to the bastion hosts.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        description: str = None,
        expire_time: int = None,
        image_version: str = None,
        instance_id: str = None,
        instance_status: str = None,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        legacy: bool = None,
        license_code: str = None,
        plan_code: str = None,
        public_network_access: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # The description of the bastion host.
        self.description = description
        # The timestamp when the bastion host expires. Unit: milliseconds.
        self.expire_time = expire_time
        # The image version of the bastion host.
        self.image_version = image_version
        # The ID of the bastion host.
        self.instance_id = instance_id
        # The status of the bastion host. Valid values:
        # 
        # *   **PENDING**: The bastion host is not initialized.
        # *   **CREATING**: The bastion host is being created.
        # *   **RUNNING**: The bastion host is running.
        # *   **EXPIRED**: The bastion host expired.
        # *   **CREATE_FAILED**: The bastion host fails to be created.
        # *   **UPGRADING**: The configurations of the bastion host are being changed.
        # *   **UPGRADE_FAILED**: The configurations of the bastion host fail to be changed.
        self.instance_status = instance_status
        # The public O\&M address of the bastion host.
        self.internet_endpoint = internet_endpoint
        # The private O\&M address of the bastion host.
        self.intranet_endpoint = intranet_endpoint
        # Indicates whether the bastion host runs an earlier version. Valid values:
        # 
        # *   **true**: indicates that the bastion host runs V2 or V3.1.
        # *   **false**:indicates that the bastion host runs V3.2.
        self.legacy = legacy
        # The license code of the bastion host.
        self.license_code = license_code
        # The edition of the bastion host. Valid values:
        # 
        # *   **cloudbastion**: Basic
        # *   **cloudbastion_ha**: Enterprise
        self.plan_code = plan_code
        # Indicates whether the bastion host can be accessed from the Internet. Valid values:
        # 
        # *   **true**: The bastion host can be accessed from the Internet.
        # *   **false**: The bastion host cannot be accessed from the Internet.
        self.public_network_access = public_network_access
        # The region ID of the bastion host.
        self.region_id = region_id
        # The ID of the resource group to which the bastion host belongs.
        self.resource_group_id = resource_group_id
        # The timestamp when the bastion host is purchased or renewed. Unit: milliseconds.
        self.start_time = start_time
        # The ID of the virtual private cloud (VPC) to which the bastion host belongs.
        self.vpc_id = vpc_id
        # The ID of the vSwitch to which the bastion host belongs.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.legacy is not None:
            result['Legacy'] = self.legacy
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.plan_code is not None:
            result['PlanCode'] = self.plan_code
        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('Legacy') is not None:
            self.legacy = m.get('Legacy')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('PlanCode') is not None:
            self.plan_code = m.get('PlanCode')
        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the queried bastion hosts.
        self.instances = instances
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of bastion hosts that are queried.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstancesResponseBody = None,
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        region_id: str = None,
    ):
        # The ID of the region.
        self.accept_language = accept_language
        # The ID of request.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # DescribeRegions
        self.regions = regions
        # Queries available regions where you can create bastion hosts.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostAccountsFromHostShareKeyRequest(TeaModel):
    def __init__(
        self,
        host_account_ids: str = None,
        host_share_key_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The IDs of the host accounts.
        self.host_account_ids = host_account_ids
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_ids is not None:
            result['HostAccountIds'] = self.host_account_ids
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountIds') is not None:
            self.host_account_ids = m.get('HostAccountIds')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachHostAccountsFromHostShareKeyResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_id: str = None,
        host_share_key_id: str = None,
        message: str = None,
    ):
        # The error code returned. If **OK** is returned, the disassociation was successful. If a different error code is returned, the disassociation failed.
        self.code = code
        # The ID of the host account.
        self.host_account_id = host_account_id
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The error message returned.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DetachHostAccountsFromHostShareKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[DetachHostAccountsFromHostShareKeyResponseBodyResults] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = DetachHostAccountsFromHostShareKeyResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetachHostAccountsFromHostShareKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachHostAccountsFromHostShareKeyResponseBody = None,
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
            temp_model = DetachHostAccountsFromHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostAccountsFromUserRequest(TeaModel):
    def __init__(
        self,
        hosts: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The IDs of the host and host account on which you want to revoke permissions from the user. You can specify up to 10 host IDs and up to 10 host account IDs for each host. You can specify only host IDs. In this case, the permissions on both the specified hosts and all host accounts of the hosts are revoked from the user. For more information about this parameter, see the "Description of the Hosts parameter" section of this topic.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host and the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.hosts = hosts
        # The ID of the bastion host in which you want to revoke permissions on the specified hosts and host accounts from the user.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host in which you want to revoke permissions on the specified hosts and host accounts from the user.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user from which you want to revoke permissions on the specified hosts and host accounts.
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DetachHostAccountsFromUserResponseBodyResultsHostAccounts(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_id: str = None,
        message: str = None,
    ):
        # The return code that indicates whether permissions on the specified host account were revoked from the user. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The ID of the host account.
        self.host_account_id = host_account_id
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DetachHostAccountsFromUserResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_accounts: List[DetachHostAccountsFromUserResponseBodyResultsHostAccounts] = None,
        host_id: str = None,
        message: str = None,
        user_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The result of revoking permissions on the specified host accounts from the user.
        self.host_accounts = host_accounts
        # The ID of the host.
        self.host_id = host_id
        # This parameter is deprecated.
        self.message = message
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = DetachHostAccountsFromUserResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DetachHostAccountsFromUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[DetachHostAccountsFromUserResponseBodyResults] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DetachHostAccountsFromUserResponseBody = None,
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
            temp_model = DetachHostAccountsFromUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostAccountsFromUserGroupRequest(TeaModel):
    def __init__(
        self,
        hosts: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The IDs of the host and host account on which you want to revoke permissions from the user group.
        # 
        # You can specify up to 10 host IDs and up to 10 host account IDs for each host. You can specify only host IDs. In this case, the permissions on both the specified hosts and all host accounts of the hosts are revoked from the user group. For more information about this parameter, see the "Description of the Hosts parameter" section of this topic.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host and the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.hosts = hosts
        # The ID of the bastion host in which you want to revoke permissions on the specified hosts and host accounts from the user group.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host in which you want to revoke permissions on the specified hosts and host accounts from the user group.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user group from which you want to revoke permissions on the specified hosts and host accounts.
        # 
        # >  You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_id: str = None,
        message: str = None,
    ):
        # The return code that indicates whether permissions on the specified host account were revoked from the user group. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The ID of the host account.
        self.host_account_id = host_account_id
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DetachHostAccountsFromUserGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_accounts: List[DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts] = None,
        host_id: str = None,
        message: str = None,
        user_group_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The result of revoking permissions on the specified host accounts from the user group.
        self.host_accounts = host_accounts
        # The ID of the host.
        self.host_id = host_id
        # This parameter is deprecated.
        self.message = message
        # The ID of the group.
        self.user_group_id = user_group_id

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DetachHostAccountsFromUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[DetachHostAccountsFromUserGroupResponseBodyResults] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DetachHostAccountsFromUserGroupResponseBody = None,
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
            temp_model = DetachHostAccountsFromUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostGroupAccountsFromUserRequest(TeaModel):
    def __init__(
        self,
        host_groups: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The ID of the host group and the name of the host account on which you want to revoke permissions from the user. You can specify up to 10 host group IDs and up to 10 host account names for each host group. You can specify only host group IDs. In this case, the permissions on the specified host groups and all host accounts in the host groups are revoked from the user. For more information about this parameter, see the "Description of the HostGroups parameter" section of this topic.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group and the [ListHostAccounts](~~204372~~) operation to query the name of the host account.
        self.host_groups = host_groups
        # The ID of the bastion host for which you want to revoke permissions on the specified host groups and host accounts from the user.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host for which you want to revoke permissions on the specified host groups and host accounts from the user.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user from which you want to revoke permissions on the specified host groups and host accounts.
        # 
        # > You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DetachHostGroupAccountsFromUserResponseBodyResultsHostAccountNames(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_name: str = None,
        message: str = None,
    ):
        # The return code that indicates whether permissions on the specified host account were revoked from the user. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The name of the host account.
        self.host_account_name = host_account_name
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DetachHostGroupAccountsFromUserResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_names: List[DetachHostGroupAccountsFromUserResponseBodyResultsHostAccountNames] = None,
        host_group_id: str = None,
        message: str = None,
        user_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The result of revoking permissions on the specified host accounts from the user.
        self.host_account_names = host_account_names
        # The ID of the host group.
        self.host_group_id = host_group_id
        # This parameter is deprecated.
        self.message = message
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        if self.host_account_names:
            for k in self.host_account_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k in self.host_account_names:
                result['HostAccountNames'].append(k.to_map() if k else None)
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k in m.get('HostAccountNames'):
                temp_model = DetachHostGroupAccountsFromUserResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k))
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DetachHostGroupAccountsFromUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[DetachHostGroupAccountsFromUserResponseBodyResults] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DetachHostGroupAccountsFromUserResponseBody = None,
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
            temp_model = DetachHostGroupAccountsFromUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostGroupAccountsFromUserGroupRequest(TeaModel):
    def __init__(
        self,
        host_groups: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The ID of the host group and the name of host account on which you want to revoke permissions from the user group. You can specify up to 10 host group IDs and up to 10 host account names for each host group. You can specify only host group IDs. In this case, the permissions on the specified host groups and all host accounts in the host groups are revoked from the user group. For more information about this parameter, see the "Description of the HostGroups parameter" section of this topic.
        # 
        # >  You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group and the [ListHostAccounts](~~204372~~) operation to query the name of the host account.
        self.host_groups = host_groups
        # The ID of the bastion host for which you want to revoke permissions on the specified host groups and host accounts from the user group.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host for which you want to revoke permissions on the specified host groups and host accounts from the user group.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user group from which you want to revoke permissions on the specified host groups and host accounts.
        # 
        # >  You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DetachHostGroupAccountsFromUserGroupResponseBodyResultsHostAccountNames(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_name: str = None,
        message: str = None,
    ):
        # The return code that indicates whether permissions on the specified host account were revoked from the specified user group. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The name of the host account.
        self.host_account_name = host_account_name
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DetachHostGroupAccountsFromUserGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_account_names: List[DetachHostGroupAccountsFromUserGroupResponseBodyResultsHostAccountNames] = None,
        host_group_id: str = None,
        message: str = None,
        user_group_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The result of revoking permissions on the specified host accounts from the user group.
        self.host_account_names = host_account_names
        # The ID of the host group.
        self.host_group_id = host_group_id
        # This parameter is deprecated.
        self.message = message
        # The ID of the group.
        self.user_group_id = user_group_id

    def validate(self):
        if self.host_account_names:
            for k in self.host_account_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k in self.host_account_names:
                result['HostAccountNames'].append(k.to_map() if k else None)
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k in m.get('HostAccountNames'):
                temp_model = DetachHostGroupAccountsFromUserGroupResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k))
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DetachHostGroupAccountsFromUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[DetachHostGroupAccountsFromUserGroupResponseBodyResults] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DetachHostGroupAccountsFromUserGroupResponseBody = None,
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
            temp_model = DetachHostGroupAccountsFromUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableInstancePublicAccessRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the bastion host whose Internet access you want to disable.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableInstancePublicAccessResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # The ID of the bastion host whose Internet access is disabled.
        self.instance_id = instance_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableInstancePublicAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableInstancePublicAccessResponseBody = None,
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
            temp_model = DisableInstancePublicAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableInstancePublicAccessRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the bastion host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableInstancePublicAccessResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # The ID of the bastion host whose Internet access is enabled.
        self.instance_id = instance_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableInstancePublicAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableInstancePublicAccessResponseBody = None,
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
            temp_model = EnableInstancePublicAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostRequest(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the host that you want to query. You can specify only one host ID.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.host_id = host_id
        # The ID of the bastion host in which you want to query the host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host in which you want to query the host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetHostResponseBodyHostProtocols(TeaModel):
    def __init__(
        self,
        host_finger_print: str = None,
        port: int = None,
        protocol_name: str = None,
    ):
        # The fingerprint of the host. This parameter uniquely identifies a host.
        self.host_finger_print = host_finger_print
        # The service port of the host.
        self.port = port
        # The protocol that is used to connect to the host. Valid values:
        # 
        # *   **SSH**\
        # *   **RDP**\
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_finger_print is not None:
            result['HostFingerPrint'] = self.host_finger_print
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostFingerPrint') is not None:
            self.host_finger_print = m.get('HostFingerPrint')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class GetHostResponseBodyHost(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        host_id: str = None,
        host_name: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        network_domain_id: str = None,
        ostype: str = None,
        protocols: List[GetHostResponseBodyHostProtocols] = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_state: str = None,
    ):
        # The address type of the host. Valid values:
        # 
        # *   **Public**: a public address
        # *   **Private**: a private address
        self.active_address_type = active_address_type
        # The description of the host.
        self.comment = comment
        # The ID of the host.
        self.host_id = host_id
        # The hostname.
        self.host_name = host_name
        # The internal endpoint of the host. The value is a domain name or an IP address.
        self.host_private_address = host_private_address
        # The public address of the host. The value is a domain name or an IP address.
        self.host_public_address = host_public_address
        # The ID of the new network domain to which the host belongs.
        self.network_domain_id = network_domain_id
        # The operating system of the host. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.ostype = ostype
        # The protocol information about the host.
        self.protocols = protocols
        # The source of the host. Valid values:
        # 
        # *   **Local**: a host in a data center
        # *   **Ecs**: an Elastic Compute Service (ECS) instance
        # *   **Rds**: a host in an ApsaraDB MyBase dedicated cluster
        self.source = source
        # The ID of the ECS instance or the host in an ApsaraDB MyBase dedicated cluster.
        # 
        # >  If **Local** is returned for the **Source** parameter, no value is returned for this parameter.
        self.source_instance_id = source_instance_id
        # The status of the host. Valid values:
        # 
        # *   **Normal**: normal
        # *   **Release**: released
        self.source_instance_state = source_instance_state

    def validate(self):
        if self.protocols:
            for k in self.protocols:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.ostype is not None:
            result['OSType'] = self.ostype
        result['Protocols'] = []
        if self.protocols is not None:
            for k in self.protocols:
                result['Protocols'].append(k.to_map() if k else None)
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        self.protocols = []
        if m.get('Protocols') is not None:
            for k in m.get('Protocols'):
                temp_model = GetHostResponseBodyHostProtocols()
                self.protocols.append(temp_model.from_map(k))
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')
        return self


class GetHostResponseBody(TeaModel):
    def __init__(
        self,
        host: GetHostResponseBodyHost = None,
        request_id: str = None,
    ):
        # The information about the host that was queried.
        self.host = host
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.host:
            self.host.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            temp_model = GetHostResponseBodyHost()
            self.host = temp_model.from_map(m['Host'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHostResponseBody = None,
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
            temp_model = GetHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostAccountRequest(TeaModel):
    def __init__(
        self,
        host_account_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the host account that you want to query.
        # 
        # > You can call the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.host_account_id = host_account_id
        # The ID of the bastion host in which you want to query the details of the host account.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host in which you want to query the details of the host account.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetHostAccountResponseBodyHostAccount(TeaModel):
    def __init__(
        self,
        has_password: bool = None,
        host_account_id: str = None,
        host_account_name: str = None,
        host_id: str = None,
        host_share_key_id: str = None,
        host_share_key_name: str = None,
        private_key_fingerprint: str = None,
        protocol_name: str = None,
    ):
        # Indicates whether a password is configured for the host account. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.has_password = has_password
        # The ID of the host account.
        self.host_account_id = host_account_id
        # The name of the host account.
        self.host_account_name = host_account_name
        # The ID of the host to which the host account belongs.
        self.host_id = host_id
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The name of the shared key.
        self.host_share_key_name = host_share_key_name
        # The fingerprint of the private key.
        self.private_key_fingerprint = private_key_fingerprint
        # The protocol that is used by the host. Valid values:
        # 
        # *   **SSH**\
        # *   **RDP**\
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name
        if self.private_key_fingerprint is not None:
            result['PrivateKeyFingerprint'] = self.private_key_fingerprint
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')
        if m.get('PrivateKeyFingerprint') is not None:
            self.private_key_fingerprint = m.get('PrivateKeyFingerprint')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class GetHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        host_account: GetHostAccountResponseBodyHostAccount = None,
        request_id: str = None,
    ):
        # The details of the host account that was queried.
        self.host_account = host_account
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.host_account:
            self.host_account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account is not None:
            result['HostAccount'] = self.host_account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccount') is not None:
            temp_model = GetHostAccountResponseBodyHostAccount()
            self.host_account = temp_model.from_map(m['HostAccount'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHostAccountResponseBody = None,
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
            temp_model = GetHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostGroupRequest(TeaModel):
    def __init__(
        self,
        host_group_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The region ID of the Bastionhost instance where you want to query the host group.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.host_group_id = host_group_id
        # MyHostGroup
        self.instance_id = instance_id
        # The ID of the Bastionhost instance where you want to query the host group.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetHostGroupResponseBodyHostGroup(TeaModel):
    def __init__(
        self,
        comment: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
    ):
        # The details of the host group returned.
        self.comment = comment
        # The description of the host group.
        self.host_group_id = host_group_id
        # The ID of the host group.
        self.host_group_name = host_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        host_group: GetHostGroupResponseBodyHostGroup = None,
        request_id: str = None,
    ):
        # The ID of the host group that you want to query.
        # 
        # >  You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group = host_group
        # my host group.
        self.request_id = request_id

    def validate(self):
        if self.host_group:
            self.host_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group is not None:
            result['HostGroup'] = self.host_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroup') is not None:
            temp_model = GetHostGroupResponseBodyHostGroup()
            self.host_group = temp_model.from_map(m['HostGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHostGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHostGroupResponseBody = None,
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
            temp_model = GetHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostShareKeyRequest(TeaModel):
    def __init__(
        self,
        host_share_key_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The time when the information about the shared key was last modified.
        self.host_share_key_id = host_share_key_id
        # The ID of the shared key whose details you want to query.
        self.instance_id = instance_id
        # The name of the shared key.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetHostShareKeyResponseBodyHostShareKey(TeaModel):
    def __init__(
        self,
        host_share_key_id: str = None,
        host_share_key_name: str = None,
        last_modify_key_at: int = None,
        private_key_finger_print: str = None,
    ):
        # The fingerprint of the private key.
        self.host_share_key_id = host_share_key_id
        self.host_share_key_name = host_share_key_name
        self.last_modify_key_at = last_modify_key_at
        self.private_key_finger_print = private_key_finger_print

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name
        if self.last_modify_key_at is not None:
            result['LastModifyKeyAt'] = self.last_modify_key_at
        if self.private_key_finger_print is not None:
            result['PrivateKeyFingerPrint'] = self.private_key_finger_print
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')
        if m.get('LastModifyKeyAt') is not None:
            self.last_modify_key_at = m.get('LastModifyKeyAt')
        if m.get('PrivateKeyFingerPrint') is not None:
            self.private_key_finger_print = m.get('PrivateKeyFingerPrint')
        return self


class GetHostShareKeyResponseBody(TeaModel):
    def __init__(
        self,
        host_share_key: GetHostShareKeyResponseBodyHostShareKey = None,
        request_id: str = None,
    ):
        # The operation that you want to perform. Set the value to **GetHostShareKey**.
        self.host_share_key = host_share_key
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.host_share_key:
            self.host_share_key.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key is not None:
            result['HostShareKey'] = self.host_share_key.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostShareKey') is not None:
            temp_model = GetHostShareKeyResponseBodyHostShareKey()
            self.host_share_key = temp_model.from_map(m['HostShareKey'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHostShareKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHostShareKeyResponseBody = None,
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
            temp_model = GetHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceADAuthServerRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The field that is used to indicate the email address of a user on the AD server.
        self.instance_id = instance_id
        # Indicates whether passwords are required. Valid values:
        # 
        # *   **true**: required
        # *   **false**: not required
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetInstanceADAuthServerResponseBodyAD(TeaModel):
    def __init__(
        self,
        account: str = None,
        base_dn: str = None,
        domain: str = None,
        email_mapping: str = None,
        filter: str = None,
        has_password: bool = None,
        is_ssl: bool = None,
        mobile_mapping: str = None,
        name_mapping: str = None,
        port: int = None,
        server: str = None,
        standby_server: str = None,
    ):
        # The port that is used to access the AD server.
        self.account = account
        # The ID of the bastion host to query.
        # 
        # You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.base_dn = base_dn
        # The settings of AD authentication.
        self.domain = domain
        # The address of the secondary AD server.
        self.email_mapping = email_mapping
        # The field that is used to indicate the mobile phone number of a user on the AD server.
        self.filter = filter
        # The address of the AD server.
        self.has_password = has_password
        # The Base DN of the AD server.
        self.is_ssl = is_ssl
        # The field that is used to indicate the name of a user on the AD server.
        self.mobile_mapping = mobile_mapping
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.name_mapping = name_mapping
        # Queries the settings of Active Directory (AD) authentication on a bastion host.
        self.port = port
        self.server = server
        self.standby_server = standby_server

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.email_mapping is not None:
            result['EmailMapping'] = self.email_mapping
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl
        if self.mobile_mapping is not None:
            result['MobileMapping'] = self.mobile_mapping
        if self.name_mapping is not None:
            result['NameMapping'] = self.name_mapping
        if self.port is not None:
            result['Port'] = self.port
        if self.server is not None:
            result['Server'] = self.server
        if self.standby_server is not None:
            result['StandbyServer'] = self.standby_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EmailMapping') is not None:
            self.email_mapping = m.get('EmailMapping')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')
        if m.get('MobileMapping') is not None:
            self.mobile_mapping = m.get('MobileMapping')
        if m.get('NameMapping') is not None:
            self.name_mapping = m.get('NameMapping')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('StandbyServer') is not None:
            self.standby_server = m.get('StandbyServer')
        return self


class GetInstanceADAuthServerResponseBody(TeaModel):
    def __init__(
        self,
        ad: GetInstanceADAuthServerResponseBodyAD = None,
        request_id: str = None,
    ):
        # The operation that you want to perform. Set the value to **GetInstanceADAuthServer**.
        self.ad = ad
        # Indicates whether SSL is supported. Valid values:
        # 
        # *   **true**: supported
        # *   **false**: not supported
        self.request_id = request_id

    def validate(self):
        if self.ad:
            self.ad.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad is not None:
            result['AD'] = self.ad.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AD') is not None:
            temp_model = GetInstanceADAuthServerResponseBodyAD()
            self.ad = temp_model.from_map(m['AD'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceADAuthServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceADAuthServerResponseBody = None,
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
            temp_model = GetInstanceADAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceLDAPAuthServerRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Indicates whether passwords are required. Valid values:
        # 
        # *   **true**: required
        # *   **false**: not required
        self.instance_id = instance_id
        # The operation that you want to perform. Set the value to **GetInstanceLDAPAuthServer**.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetInstanceLDAPAuthServerResponseBodyLDAP(TeaModel):
    def __init__(
        self,
        account: str = None,
        base_dn: str = None,
        email_mapping: str = None,
        filter: str = None,
        has_password: str = None,
        is_ssl: bool = None,
        login_name_mapping: str = None,
        mobile_mapping: str = None,
        name_mapping: str = None,
        port: int = None,
        server: str = None,
        standby_server: str = None,
    ):
        # The ID of the bastion host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.account = account
        # The field that is used to indicate the logon name of a user on the LDAP server.
        self.base_dn = base_dn
        # The address of the secondary LDAP server.
        self.email_mapping = email_mapping
        # The Base distinguished name (DN).
        self.filter = filter
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.has_password = has_password
        # The condition that is used to filter users.
        self.is_ssl = is_ssl
        # The port that is used to access the LDAP server.
        self.login_name_mapping = login_name_mapping
        # The field that is used to indicate the email address of a user on the LDAP server.
        self.mobile_mapping = mobile_mapping
        # The field that is used to indicate the mobile phone number of a user on the LDAP server.
        self.name_mapping = name_mapping
        self.port = port
        self.server = server
        self.standby_server = standby_server

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn
        if self.email_mapping is not None:
            result['EmailMapping'] = self.email_mapping
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl
        if self.login_name_mapping is not None:
            result['LoginNameMapping'] = self.login_name_mapping
        if self.mobile_mapping is not None:
            result['MobileMapping'] = self.mobile_mapping
        if self.name_mapping is not None:
            result['NameMapping'] = self.name_mapping
        if self.port is not None:
            result['Port'] = self.port
        if self.server is not None:
            result['Server'] = self.server
        if self.standby_server is not None:
            result['StandbyServer'] = self.standby_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')
        if m.get('EmailMapping') is not None:
            self.email_mapping = m.get('EmailMapping')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')
        if m.get('LoginNameMapping') is not None:
            self.login_name_mapping = m.get('LoginNameMapping')
        if m.get('MobileMapping') is not None:
            self.mobile_mapping = m.get('MobileMapping')
        if m.get('NameMapping') is not None:
            self.name_mapping = m.get('NameMapping')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('StandbyServer') is not None:
            self.standby_server = m.get('StandbyServer')
        return self


class GetInstanceLDAPAuthServerResponseBody(TeaModel):
    def __init__(
        self,
        ldap: GetInstanceLDAPAuthServerResponseBodyLDAP = None,
        request_id: str = None,
    ):
        # Indicates whether SSL is supported. Valid values:
        # 
        # *   **true**: supported
        # *   **false**: not supported
        self.ldap = ldap
        # The settings of LDAP authentication.
        self.request_id = request_id

    def validate(self):
        if self.ldap:
            self.ldap.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ldap is not None:
            result['LDAP'] = self.ldap.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LDAP') is not None:
            temp_model = GetInstanceLDAPAuthServerResponseBodyLDAP()
            self.ldap = temp_model.from_map(m['LDAP'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceLDAPAuthServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceLDAPAuthServerResponseBody = None,
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
            temp_model = GetInstanceLDAPAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceTwoFactorRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.instance_id = instance_id
        # The operation that you want to perform. Set the value to **GetInstanceTwoFactor**.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetInstanceTwoFactorResponseBodyConfig(TeaModel):
    def __init__(
        self,
        enable_two_factor: bool = None,
        skip_two_factor_time: int = None,
        two_factor_methods: List[str] = None,
    ):
        # Queries the settings of two-factor authentication on a bastion host.
        self.enable_two_factor = enable_two_factor
        self.skip_two_factor_time = skip_two_factor_time
        self.two_factor_methods = two_factor_methods

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_two_factor is not None:
            result['EnableTwoFactor'] = self.enable_two_factor
        if self.skip_two_factor_time is not None:
            result['SkipTwoFactorTime'] = self.skip_two_factor_time
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTwoFactor') is not None:
            self.enable_two_factor = m.get('EnableTwoFactor')
        if m.get('SkipTwoFactorTime') is not None:
            self.skip_two_factor_time = m.get('SkipTwoFactorTime')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        return self


class GetInstanceTwoFactorResponseBody(TeaModel):
    def __init__(
        self,
        config: GetInstanceTwoFactorResponseBodyConfig = None,
        request_id: str = None,
    ):
        # The settings of two-factor authentication.
        self.config = config
        # The duration within which two-factor authentication is not required after a local user passes two-factor authentication. Valid values: `0 to 168`. Unit: hours.
        # 
        # >  If 0 is returned, a local user must pass two-factor authentication every time the local user logs on to the bastion host.
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
            temp_model = GetInstanceTwoFactorResponseBodyConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceTwoFactorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceTwoFactorResponseBody = None,
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
            temp_model = GetInstanceTwoFactorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The ID of the bastion host on which you want to query the user.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host on which you want to query the user.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user.
        # 
        # > You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        comment: str = None,
        display_name: str = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        email: str = None,
        language: str = None,
        language_status: str = None,
        mobile: str = None,
        mobile_country_code: str = None,
        need_reset_password: bool = None,
        source: str = None,
        source_user_id: str = None,
        two_factor_methods: List[str] = None,
        two_factor_status: str = None,
        user_id: str = None,
        user_name: str = None,
        user_state: List[str] = None,
    ):
        # The description of the user.
        self.comment = comment
        # The display name of the user.
        self.display_name = display_name
        # The end of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time
        # The beginning of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time
        # The email address of the user.
        self.email = email
        self.language = language
        self.language_status = language_status
        # The mobile phone number of the user.
        self.mobile = mobile
        # The location in which the mobile number of the user is registered. Valid values:
        # 
        # *   **CN**: the Chinese mainland, whose country calling code is +86
        # *   **HK**: Hong Kong (China), whose country calling code is +852
        # *   **MO**: Macao (China), whose country calling code is +853
        # *   **TW**: Taiwan (China), whose country calling code is +886
        # *   **RU**: Russia, whose country calling code is +7
        # *   **SG**: Singapore, whose country calling code is +65
        # *   **MY**: Malaysia, whose country calling code is +60
        # *   **ID**: Indonesia, whose country calling code is +62
        # *   **DE**: Germany, whose country calling code is +49
        # *   **AU**: Australia, whose country calling code is +61
        # *   **US**: US, whose country calling code is +1
        # *   **AE**: United Arab Emirates, whose country calling code is +971
        # *   **JP:** Japan, whose country calling code is +81
        # *   **GB**: UK, whose country calling code is +44
        # *   **IN**: India, whose country calling code is +91
        # *   **KR**: Republic of Korea, whose country calling code is +82
        # *   **PH**: Philippines, whose country calling code is +63
        # *   **CH**: Switzerland, whose country calling code is +41
        # *   **SE**: Sweden, whose country calling code is +46
        self.mobile_country_code = mobile_country_code
        # Specifies whether password reset is required upon the next logon. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.need_reset_password = need_reset_password
        # The source of the user. Valid values:
        # 
        # *   **Local**: a local user
        # *   **Ram**: a RAM user
        self.source = source
        # The unique ID of the user.
        # 
        # > This parameter uniquely identifies a RAM user of the bastion host. A value is returned for this parameter if the **Source** parameter is set to **Ram**. No value is returned for this parameter if the **Source** parameter is set to **Local**.
        self.source_user_id = source_user_id
        # An array that consists of the details of the two-factor authentication method.
        self.two_factor_methods = two_factor_methods
        # The two-factor authentication status of the user. Valid values:
        # 
        # *   **Global**: The global settings are used.
        # *   **Disable**: The two-factor authentication is disabled.
        # *   **Enable**: The two-factor authentication is enabled and the user-specific setting is used.
        self.two_factor_status = two_factor_status
        # The ID of the user.
        self.user_id = user_id
        # The logon name of the user.
        self.user_name = user_name
        # An array that consists of the details of the user status.
        self.user_state = user_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.email is not None:
            result['Email'] = self.email
        if self.language is not None:
            result['Language'] = self.language
        if self.language_status is not None:
            result['LanguageStatus'] = self.language_status
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.need_reset_password is not None:
            result['NeedResetPassword'] = self.need_reset_password
        if self.source is not None:
            result['Source'] = self.source
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        if self.two_factor_status is not None:
            result['TwoFactorStatus'] = self.two_factor_status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_state is not None:
            result['UserState'] = self.user_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageStatus') is not None:
            self.language_status = m.get('LanguageStatus')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('NeedResetPassword') is not None:
            self.need_reset_password = m.get('NeedResetPassword')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        if m.get('TwoFactorStatus') is not None:
            self.two_factor_status = m.get('TwoFactorStatus')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user: GetUserResponseBodyUser = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the user that was queried.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('User') is not None:
            temp_model = GetUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
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


class GetUserGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The ID of the request.
        self.instance_id = instance_id
        # The name of the user group.
        self.region_id = region_id
        # All Bastionhost API requests must include common request parameters. For more information about common request parameters, see [Common parameters](~~315526~~).
        # 
        # For more information about sample requests, see the "Examples" section of this topic.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        # GetUserGroup
        self.comment = comment
        self.user_group_id = user_group_id
        # WB662865
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        # Queries the details of a specified user group in a specified Bastionhost instance.
        self.request_id = request_id
        # GetUserGroup
        self.user_group = user_group

    def validate(self):
        if self.user_group:
            self.user_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: GetUserGroupResponseBody = None,
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
            temp_model = GetUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApproveCommandsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListApproveCommandsResponseBodyApproveCommands(TeaModel):
    def __init__(
        self,
        approve_command_id: str = None,
        asset_account_name: str = None,
        asset_ip: str = None,
        asset_name: str = None,
        client_ip: str = None,
        client_user: str = None,
        command: str = None,
        create_time: str = None,
        protocol_name: str = None,
        session_id: str = None,
        state: str = None,
    ):
        self.approve_command_id = approve_command_id
        self.asset_account_name = asset_account_name
        self.asset_ip = asset_ip
        self.asset_name = asset_name
        self.client_ip = client_ip
        self.client_user = client_user
        self.command = command
        self.create_time = create_time
        self.protocol_name = protocol_name
        self.session_id = session_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_command_id is not None:
            result['ApproveCommandId'] = self.approve_command_id
        if self.asset_account_name is not None:
            result['AssetAccountName'] = self.asset_account_name
        if self.asset_ip is not None:
            result['AssetIp'] = self.asset_ip
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_user is not None:
            result['ClientUser'] = self.client_user
        if self.command is not None:
            result['Command'] = self.command
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveCommandId') is not None:
            self.approve_command_id = m.get('ApproveCommandId')
        if m.get('AssetAccountName') is not None:
            self.asset_account_name = m.get('AssetAccountName')
        if m.get('AssetIp') is not None:
            self.asset_ip = m.get('AssetIp')
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientUser') is not None:
            self.client_user = m.get('ClientUser')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListApproveCommandsResponseBody(TeaModel):
    def __init__(
        self,
        approve_commands: List[ListApproveCommandsResponseBodyApproveCommands] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.approve_commands = approve_commands
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.approve_commands:
            for k in self.approve_commands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApproveCommands'] = []
        if self.approve_commands is not None:
            for k in self.approve_commands:
                result['ApproveCommands'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approve_commands = []
        if m.get('ApproveCommands') is not None:
            for k in m.get('ApproveCommands'):
                temp_model = ListApproveCommandsResponseBodyApproveCommands()
                self.approve_commands.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApproveCommandsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApproveCommandsResponseBody = None,
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
            temp_model = ListApproveCommandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsRequest(TeaModel):
    def __init__(
        self,
        host_account_name: str = None,
        host_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        protocol_name: str = None,
        region_id: str = None,
    ):
        # Indicates whether a password is configured for the host account.
        # 
        # Valid values:
        # 
        # *   true: A password is configured for the host account.
        # *   false: No passwords are configured for the host account.
        self.host_account_name = host_account_name
        # The protocol used by the host whose accounts you want to query.
        # 
        # Valid values:
        # 
        # *   SSH
        # *   RDP
        self.host_id = host_id
        # The ID of the shared key.
        self.instance_id = instance_id
        # The operation that you want to perform.
        # 
        # Set the value to **ListHostAccounts**.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The name of the host account that you want to query. The name can be up to 128 characters in length. Only exact match is supported.
        self.protocol_name = protocol_name
        # The ID of the specified host whose accounts you want to query.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListHostAccountsResponseBodyHostAccounts(TeaModel):
    def __init__(
        self,
        has_password: bool = None,
        host_account_id: str = None,
        host_account_name: str = None,
        host_id: str = None,
        host_share_key_id: str = None,
        host_share_key_name: str = None,
        private_key_fingerprint: str = None,
        protocol_name: str = None,
    ):
        # The fingerprint of the private key for the host account.
        self.has_password = has_password
        # The ID of the request.
        self.host_account_id = host_account_id
        # The name of the shared key.
        self.host_account_name = host_account_name
        self.host_id = host_id
        self.host_share_key_id = host_share_key_id
        self.host_share_key_name = host_share_key_name
        # The protocol that is used by the host.
        # 
        # Valid values:
        # 
        # *   SSH
        # *   RDP
        self.private_key_fingerprint = private_key_fingerprint
        # The number of the page to return. Default value: **1**.
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name
        if self.private_key_fingerprint is not None:
            result['PrivateKeyFingerprint'] = self.private_key_fingerprint
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')
        if m.get('PrivateKeyFingerprint') is not None:
            self.private_key_fingerprint = m.get('PrivateKeyFingerprint')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class ListHostAccountsResponseBody(TeaModel):
    def __init__(
        self,
        host_accounts: List[ListHostAccountsResponseBodyHostAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The ID of the host account.
        self.host_accounts = host_accounts
        # An array that consists of the queried host accounts.
        self.request_id = request_id
        # The ID of the bastion host in which you want to query accounts of the specified host.
        # 
        # >  You can call the DescribeInstances operation to query the ID of the bastion host.
        self.total_count = total_count

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = ListHostAccountsResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostAccountsResponseBody = None,
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
            temp_model = ListHostAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsForHostShareKeyRequest(TeaModel):
    def __init__(
        self,
        host_share_key_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListHostAccountsForHostShareKeyResponseBodyHostAccounts(TeaModel):
    def __init__(
        self,
        host_account_name: str = None,
        host_id: str = None,
        hosts_account_id: str = None,
        protocol_name: str = None,
    ):
        # The name of the host account.
        self.host_account_name = host_account_name
        # The ID of the host.
        self.host_id = host_id
        # The ID of the host account.
        self.hosts_account_id = hosts_account_id
        # The O\&M protocol.
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.hosts_account_id is not None:
            result['HostsAccountId'] = self.hosts_account_id
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostsAccountId') is not None:
            self.hosts_account_id = m.get('HostsAccountId')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class ListHostAccountsForHostShareKeyResponseBody(TeaModel):
    def __init__(
        self,
        host_accounts: List[ListHostAccountsForHostShareKeyResponseBodyHostAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the host accounts that are associated with the shared key.
        self.host_accounts = host_accounts
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of the host accounts that are associated with the shared key.
        self.total_count = total_count

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = ListHostAccountsForHostShareKeyResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostAccountsForHostShareKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostAccountsForHostShareKeyResponseBody = None,
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
            temp_model = ListHostAccountsForHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsForUserRequest(TeaModel):
    def __init__(
        self,
        host_account_name: str = None,
        host_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.host_account_name = host_account_name
        # The ID of the host for which the host accounts were queried.
        self.host_id = host_id
        # The total number of host accounts returned.
        self.instance_id = instance_id
        # The ID of the user for which you want to query authorized host accounts.
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the ID of the user ID.
        self.page_number = page_number
        # The name of the host account that you want to query. Exact match is supported.
        self.page_size = page_size
        # The name of the host account.
        self.region_id = region_id
        # The region ID of the Bastionhost instance where you want to query the host accounts that the user is authorized to manage on the host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListHostAccountsForUserResponseBodyHostAccounts(TeaModel):
    def __init__(
        self,
        host_account_id: str = None,
        host_account_name: str = None,
        host_id: str = None,
        is_authorized: bool = None,
        protocol_name: str = None,
    ):
        # The protocol that is used by the host account. Valid values:
        # 
        # *   **SSH**\
        # *   **RDP**\
        self.host_account_id = host_account_id
        # The ID of the host account.
        self.host_account_name = host_account_name
        # The ID of the request.
        self.host_id = host_id
        # The ID of the host for which you want to query the host accounts that the user is authorized to manage.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.is_authorized = is_authorized
        # Indicates whether the user is authorized to manage the host account. Valid values:
        # 
        # *   **true**: The user is authorized to manage the host account.
        # *   **false**: The user is not authorized to manage the host account.
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class ListHostAccountsForUserResponseBody(TeaModel):
    def __init__(
        self,
        host_accounts: List[ListHostAccountsForUserResponseBodyHostAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The host accounts returned.
        self.host_accounts = host_accounts
        # The ID of the Bastionhost instance where you want to query the host accounts that the user is authorized to manage on the host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.request_id = request_id
        # The number of entries to return on each page.
        # 
        # The value of the PageSize parameter must not exceed 100. Default value: 20. If you leave the PageSize parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave the PageSize parameter empty.
        self.total_count = total_count

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = ListHostAccountsForUserResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostAccountsForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostAccountsForUserResponseBody = None,
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
            temp_model = ListHostAccountsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsForUserGroupRequest(TeaModel):
    def __init__(
        self,
        host_account_name: str = None,
        host_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The name of the host account that you want to query. Exact match is supported.
        self.host_account_name = host_account_name
        # The ID of the host to query.
        # 
        # > You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.host_id = host_id
        # The ID of the bastion host on which you want to query the host accounts to be managed by the specified user group on the specified host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page.\
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The region ID of the bastion host on which you want to query the host accounts to be managed by the specified user group on the specified host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user group for which you want to query authorized host accounts.
        # 
        # > You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListHostAccountsForUserGroupResponseBodyHostAccounts(TeaModel):
    def __init__(
        self,
        host_account_id: str = None,
        host_account_name: str = None,
        host_id: str = None,
        is_authorized: bool = None,
        protocol_name: str = None,
    ):
        # The ID of the host account.
        self.host_account_id = host_account_id
        # The name of the host account.
        self.host_account_name = host_account_name
        # The ID of the host for which the host accounts were queried.
        self.host_id = host_id
        # Indicates whether the user group is authorized to manage the host account. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.is_authorized = is_authorized
        # The protocol that is used by the host. Valid values:
        # 
        # *   **SSH**\
        # *   **RDP**\
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class ListHostAccountsForUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        host_accounts: List[ListHostAccountsForUserGroupResponseBodyHostAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the queried host accounts.
        self.host_accounts = host_accounts
        # The ID of the request.
        self.request_id = request_id
        # The total number of host accounts that were queried.
        self.total_count = total_count

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = ListHostAccountsForUserGroupResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostAccountsForUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostAccountsForUserGroupResponseBody = None,
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
            temp_model = ListHostAccountsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupAccountNamesForUserRequest(TeaModel):
    def __init__(
        self,
        host_group_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The ID of the host group.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_id = host_group_id
        # The ID of the bastion host to which the user belongs.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host to which the user belongs.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user.
        # 
        # > You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListHostGroupAccountNamesForUserResponseBody(TeaModel):
    def __init__(
        self,
        host_account_names: List[str] = None,
        request_id: str = None,
    ):
        # An array that consists of the names of host accounts.
        self.host_account_names = host_account_names
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_names is not None:
            result['HostAccountNames'] = self.host_account_names
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountNames') is not None:
            self.host_account_names = m.get('HostAccountNames')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHostGroupAccountNamesForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostGroupAccountNamesForUserResponseBody = None,
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
            temp_model = ListHostGroupAccountNamesForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupAccountNamesForUserGroupRequest(TeaModel):
    def __init__(
        self,
        host_group_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The ID of the host group.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_id = host_group_id
        # The ID of the bastion host on which you want to query the host account names the user group is authorized to manage in a host group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host on which you want to query the host account names the user group is authorized to manage in a host group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user group.
        # 
        # > You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListHostGroupAccountNamesForUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        host_account_names: List[str] = None,
        request_id: str = None,
    ):
        # The names of host accounts returned.
        self.host_account_names = host_account_names
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_names is not None:
            result['HostAccountNames'] = self.host_account_names
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountNames') is not None:
            self.host_account_names = m.get('HostAccountNames')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHostGroupAccountNamesForUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostGroupAccountNamesForUserGroupResponseBody = None,
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
            temp_model = ListHostGroupAccountNamesForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsRequest(TeaModel):
    def __init__(
        self,
        host_group_name: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        # The name of the host group that you want to query. Only exact match is supported.
        self.host_group_name = host_group_name
        # The ID of the bastion host in which you want to query the host group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page.\
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The region ID of the bastion host in which you want to query the host group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListHostGroupsResponseBodyHostGroups(TeaModel):
    def __init__(
        self,
        comment: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
        member_count: int = None,
    ):
        # The description of the host group.
        self.comment = comment
        # The ID of the host group.
        self.host_group_id = host_group_id
        # The name of the host group.
        self.host_group_name = host_group_name
        # The number of hosts in the host group.
        self.member_count = member_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        return self


class ListHostGroupsResponseBody(TeaModel):
    def __init__(
        self,
        host_groups: List[ListHostGroupsResponseBodyHostGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the host groups.
        self.host_groups = host_groups
        # The ID of the request.
        self.request_id = request_id
        # The total number of host groups returned.
        self.total_count = total_count

    def validate(self):
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = ListHostGroupsResponseBodyHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostGroupsResponseBody = None,
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
            temp_model = ListHostGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsForUserRequest(TeaModel):
    def __init__(
        self,
        host_group_name: str = None,
        instance_id: str = None,
        mode: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The ID of the request.
        self.host_group_name = host_group_name
        # The host groups returned.
        self.instance_id = instance_id
        # The number of entries to return on each page.
        # 
        # The value of the PageSize parameter must not exceed 100. Default value: 20. If you leave the PageSize parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave the PageSize parameter empty.
        self.mode = mode
        # The ID of the host group.
        self.page_number = page_number
        # The ID of the user.
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.page_size = page_size
        # The number of the page to return. Default value: **1**.
        self.region_id = region_id
        # The ID of the Bastionhost instance where you want to query the host groups that the user is authorized or not authorized to manage.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListHostGroupsForUserResponseBodyHostGroups(TeaModel):
    def __init__(
        self,
        comment: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
    ):
        # ListHostGroupsForUser
        self.comment = comment
        # WB662865
        self.host_group_id = host_group_id
        self.host_group_name = host_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        host_groups: List[ListHostGroupsForUserResponseBodyHostGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # ListHostGroupsForUser
        self.host_groups = host_groups
        # Queries the host groups that a specified user is authorized or not authorized to manage.
        self.request_id = request_id
        # All Bastionhost API requests must include common request parameters. For more information about common request parameters, see [Common parameters](~~148139~~).
        # 
        # For more information about sample requests, see the "Examples" section of this topic.
        self.total_count = total_count

    def validate(self):
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = ListHostGroupsForUserResponseBodyHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostGroupsForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostGroupsForUserResponseBody = None,
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
            temp_model = ListHostGroupsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsForUserGroupRequest(TeaModel):
    def __init__(
        self,
        host_group_name: str = None,
        instance_id: str = None,
        mode: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The name of the host group that you want to query. Only exact match is supported.
        self.host_group_name = host_group_name
        # The ID of the bastion host to which the user group belongs.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # Specifies the category of the host group that you want to query. Valid values:
        # 
        # *   **Authorized**: queries the host groups that the user group is authorized to manage. This is the default value.
        # *   **Unauthorized**: queries the host groups that the user group is not authorized to manage.
        self.mode = mode
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page.\
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The region ID of the bastion host to which the user group belongs.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user group.
        # 
        # > You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListHostGroupsForUserGroupResponseBodyHostGroups(TeaModel):
    def __init__(
        self,
        comment: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
    ):
        # The description of the host group.
        self.comment = comment
        # The ID of the host group.
        self.host_group_id = host_group_id
        # The name of the host group.
        self.host_group_name = host_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        host_groups: List[ListHostGroupsForUserGroupResponseBodyHostGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The host groups returned.
        self.host_groups = host_groups
        # The ID of the request.
        self.request_id = request_id
        # The total number of host groups returned.
        self.total_count = total_count

    def validate(self):
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = ListHostGroupsForUserGroupResponseBodyHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostGroupsForUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostGroupsForUserGroupResponseBody = None,
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
            temp_model = ListHostGroupsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostShareKeysRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListHostShareKeysResponseBodyHostShareKeys(TeaModel):
    def __init__(
        self,
        host_account_count: int = None,
        host_share_key_id: str = None,
        host_share_key_name: str = None,
        last_modify_key_at: int = None,
        private_key_finger_print: str = None,
    ):
        # The number of the associated host accounts.
        self.host_account_count = host_account_count
        # The ID of the host account.
        self.host_share_key_id = host_share_key_id
        # The name of the shared key.
        self.host_share_key_name = host_share_key_name
        # The time when the shared key was last modified.
        self.last_modify_key_at = last_modify_key_at
        # The fingerprint of the private key.
        self.private_key_finger_print = private_key_finger_print

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_count is not None:
            result['HostAccountCount'] = self.host_account_count
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name
        if self.last_modify_key_at is not None:
            result['LastModifyKeyAt'] = self.last_modify_key_at
        if self.private_key_finger_print is not None:
            result['PrivateKeyFingerPrint'] = self.private_key_finger_print
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountCount') is not None:
            self.host_account_count = m.get('HostAccountCount')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')
        if m.get('LastModifyKeyAt') is not None:
            self.last_modify_key_at = m.get('LastModifyKeyAt')
        if m.get('PrivateKeyFingerPrint') is not None:
            self.private_key_finger_print = m.get('PrivateKeyFingerPrint')
        return self


class ListHostShareKeysResponseBody(TeaModel):
    def __init__(
        self,
        host_share_keys: List[ListHostShareKeysResponseBodyHostShareKeys] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the shared keys.
        self.host_share_keys = host_share_keys
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of the shared keys.
        self.total_count = total_count

    def validate(self):
        if self.host_share_keys:
            for k in self.host_share_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostShareKeys'] = []
        if self.host_share_keys is not None:
            for k in self.host_share_keys:
                result['HostShareKeys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_share_keys = []
        if m.get('HostShareKeys') is not None:
            for k in m.get('HostShareKeys'):
                temp_model = ListHostShareKeysResponseBodyHostShareKeys()
                self.host_share_keys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostShareKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostShareKeysResponseBody = None,
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
            temp_model = ListHostShareKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostsRequest(TeaModel):
    def __init__(
        self,
        host_address: str = None,
        host_group_id: str = None,
        host_name: str = None,
        instance_id: str = None,
        ostype: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_state: str = None,
    ):
        # The address of the host that you want to query. You can set this parameter to a domain name or an IP address. Only exact match is supported.
        self.host_address = host_address
        # The ID of the host group to which the host to be queried belongs.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_id = host_group_id
        # The name of the host that you want to query. Only exact match is supported.
        self.host_name = host_name
        # The ID of the bastion host on which you want to query hosts.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The operating system of the host that you want to query. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.ostype = ostype
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **10**.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The region ID of the bastion host on which you want to query hosts.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The source of the host that you want to query. Valid values:
        # 
        # *   **Local**: a host in a data center
        # *   **Ecs**: an Elastic Compute Service (ECS) instance
        # *   **Rds**: a host in an ApsaraDB MyBase dedicated cluster
        self.source = source
        # The ID of the ECS instance or the host in an ApsaraDB MyBase dedicated cluster that you want to query. Only exact match is supported.
        self.source_instance_id = source_instance_id
        # The status of the host that you want to query. Valid values:
        # 
        # *   **Normal**: normal
        # *   **Release**: released
        self.source_instance_state = source_instance_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')
        return self


class ListHostsResponseBodyHosts(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        host_account_count: int = None,
        host_id: str = None,
        host_name: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        ostype: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_state: str = None,
    ):
        # The address type of the host. Valid values:
        # 
        # *   **Public**: a public address
        # *   **Private**: a private address
        self.active_address_type = active_address_type
        # The description of the host.
        self.comment = comment
        # The number of host accounts.
        self.host_account_count = host_account_count
        # The ID of the host.
        self.host_id = host_id
        # The name of the host.
        self.host_name = host_name
        # The private address of the host. The value is a domain name or an IP address.
        self.host_private_address = host_private_address
        # The public address of the host. The value is a domain name or an IP address.
        self.host_public_address = host_public_address
        # The operating system of the host. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.ostype = ostype
        # The source of the host. Valid values:
        # 
        # *   **Local**: a host in a data center
        # *   **Ecs**: an ECS instance
        # *   **Rds**: a host in an ApsaraDB MyBase dedicated cluster
        self.source = source
        # The ID of the ECS instance or the host in an ApsaraDB MyBase dedicated cluster.
        # 
        # > No value is returned for this parameter if the **Source** parameter is set to **Local**.
        self.source_instance_id = source_instance_id
        # The status of the host. Valid values:
        # 
        # *   **Normal**: normal
        # *   **Release**: released
        self.source_instance_state = source_instance_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_account_count is not None:
            result['HostAccountCount'] = self.host_account_count
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostAccountCount') is not None:
            self.host_account_count = m.get('HostAccountCount')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')
        return self


class ListHostsResponseBody(TeaModel):
    def __init__(
        self,
        hosts: List[ListHostsResponseBodyHosts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the hosts returned.
        self.hosts = hosts
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of hosts returned.
        self.total_count = total_count

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = ListHostsResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostsResponseBody = None,
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
            temp_model = ListHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostsForUserRequest(TeaModel):
    def __init__(
        self,
        host_address: str = None,
        host_name: str = None,
        instance_id: str = None,
        mode: str = None,
        ostype: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The endpoint of the host that you want to query. You can set this parameter to a domain name or an IP address. Only exact match is supported.
        self.host_address = host_address
        # The name of the host that you want to query. Only exact match is supported.
        self.host_name = host_name
        # The ID of the bastion host on which you want to query the hosts that the user is authorized or not authorized to manage.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # Specifies the category of the hosts that you want to query. Valid values:
        # 
        # *   **Authorized**: queries the hosts that the user is authorized to manage. This is the default value.
        # *   **Unauthorized**: queries the hosts that the user is not authorized to manage.
        self.mode = mode
        # The operating system of the host that you want to query. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.ostype = ostype
        # The number of the page. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.\
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned per page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The region ID of the bastion host on which you want to query the hosts that the user is authorized or not authorized to manage.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user.
        # 
        # > You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListHostsForUserResponseBodyHosts(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        host_id: str = None,
        host_name: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        ostype: str = None,
    ):
        # The endpoint type of the host. Valid values:
        # 
        # *   **Public**: public endpoint
        # *   **Private**: internal endpoint
        self.active_address_type = active_address_type
        # The description of the host.
        self.comment = comment
        # The ID of the host.
        self.host_id = host_id
        # The name of the host.
        self.host_name = host_name
        # The internal endpoint of the host. The value is a domain name or an IP address.
        self.host_private_address = host_private_address
        # The public endpoint of the host. The value is a domain name or an IP address.
        self.host_public_address = host_public_address
        # The operating system of the host. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.ostype = ostype

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.ostype is not None:
            result['OSType'] = self.ostype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        return self


class ListHostsForUserResponseBody(TeaModel):
    def __init__(
        self,
        hosts: List[ListHostsForUserResponseBodyHosts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The hosts returned.
        self.hosts = hosts
        # The request ID.
        self.request_id = request_id
        # The total number of hosts returned.
        self.total_count = total_count

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = ListHostsForUserResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostsForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostsForUserResponseBody = None,
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
            temp_model = ListHostsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostsForUserGroupRequest(TeaModel):
    def __init__(
        self,
        host_address: str = None,
        host_name: str = None,
        instance_id: str = None,
        mode: str = None,
        ostype: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The operating system of the host that you want to query. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.host_address = host_address
        # The ID of the Bastionhost instance where you want to query the hosts that the user group is authorized or not authorized to manage.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.host_name = host_name
        # The category of the host that you want to query. Valid values:
        # 
        # *   **Authorized**: Query the hosts that the user group is authorized to manage. This is the default value.
        # *   **Unauthorized**: Query the hosts that the user group is not authorized to manage.
        self.instance_id = instance_id
        # The operating system of the host. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.mode = mode
        # The internal endpoint of the host. The value is a domain name or an IP address.
        self.ostype = ostype
        # The endpoint type of the host. Valid values:
        # 
        # *   **Public**: a public endpoint
        # *   **Private**: an internal endpoint
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # The value of the PageSize parameter must not exceed 100. Default value: 20. If you leave the PageSize parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave the PageSize parameter empty.
        self.page_size = page_size
        # The endpoint of the host that you want to query. You can set this parameter to a domain name or an IP address. Only exact match is supported.
        self.region_id = region_id
        # The number of the page to return. Default value: 1.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListHostsForUserGroupResponseBodyHosts(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        host_id: str = None,
        host_name: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        ostype: str = None,
    ):
        # All Bastionhost API requests must include common request parameters. For more information about common request parameters, see [Common parameters](~~148139~~).
        # 
        # For more information about sample requests, see the "Examples" section of this topic.
        self.active_address_type = active_address_type
        # The ID of the request.
        self.comment = comment
        self.host_id = host_id
        # ListHostsForUserGroup
        self.host_name = host_name
        # WB662865
        self.host_private_address = host_private_address
        # Queries the hosts that a specified user group is authorized or not authorized to manage.
        self.host_public_address = host_public_address
        # ListHostsForUserGroup
        self.ostype = ostype

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.ostype is not None:
            result['OSType'] = self.ostype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        return self


class ListHostsForUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        hosts: List[ListHostsForUserGroupResponseBodyHosts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The ID of the user group for which you want to query hosts.
        # 
        # >  You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.hosts = hosts
        # The hosts returned.
        self.request_id = request_id
        # The public endpoint of the host. The value is a domain name or an IP address.
        self.total_count = total_count

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = ListHostsForUserGroupResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostsForUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHostsForUserGroupResponseBody = None,
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
            temp_model = ListHostsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOperationTicketsRequest(TeaModel):
    def __init__(
        self,
        asset_address: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.asset_address = asset_address
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_address is not None:
            result['AssetAddress'] = self.asset_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetAddress') is not None:
            self.asset_address = m.get('AssetAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListOperationTicketsResponseBodyOperationTickets(TeaModel):
    def __init__(
        self,
        apply_user_id: str = None,
        apply_username: str = None,
        asset_account_id: str = None,
        asset_account_name: str = None,
        asset_address: str = None,
        asset_id: str = None,
        asset_name: str = None,
        asset_network_domain_id: str = None,
        asset_os: str = None,
        asset_source: str = None,
        asset_source_instance_id: str = None,
        created_time: int = None,
        operation_ticket_id: str = None,
        protocol_name: str = None,
        state: str = None,
    ):
        self.apply_user_id = apply_user_id
        self.apply_username = apply_username
        self.asset_account_id = asset_account_id
        self.asset_account_name = asset_account_name
        self.asset_address = asset_address
        self.asset_id = asset_id
        self.asset_name = asset_name
        self.asset_network_domain_id = asset_network_domain_id
        self.asset_os = asset_os
        self.asset_source = asset_source
        self.asset_source_instance_id = asset_source_instance_id
        self.created_time = created_time
        self.operation_ticket_id = operation_ticket_id
        self.protocol_name = protocol_name
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_user_id is not None:
            result['ApplyUserId'] = self.apply_user_id
        if self.apply_username is not None:
            result['ApplyUsername'] = self.apply_username
        if self.asset_account_id is not None:
            result['AssetAccountId'] = self.asset_account_id
        if self.asset_account_name is not None:
            result['AssetAccountName'] = self.asset_account_name
        if self.asset_address is not None:
            result['AssetAddress'] = self.asset_address
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.asset_network_domain_id is not None:
            result['AssetNetworkDomainId'] = self.asset_network_domain_id
        if self.asset_os is not None:
            result['AssetOs'] = self.asset_os
        if self.asset_source is not None:
            result['AssetSource'] = self.asset_source
        if self.asset_source_instance_id is not None:
            result['AssetSourceInstanceId'] = self.asset_source_instance_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.operation_ticket_id is not None:
            result['OperationTicketId'] = self.operation_ticket_id
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyUserId') is not None:
            self.apply_user_id = m.get('ApplyUserId')
        if m.get('ApplyUsername') is not None:
            self.apply_username = m.get('ApplyUsername')
        if m.get('AssetAccountId') is not None:
            self.asset_account_id = m.get('AssetAccountId')
        if m.get('AssetAccountName') is not None:
            self.asset_account_name = m.get('AssetAccountName')
        if m.get('AssetAddress') is not None:
            self.asset_address = m.get('AssetAddress')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('AssetNetworkDomainId') is not None:
            self.asset_network_domain_id = m.get('AssetNetworkDomainId')
        if m.get('AssetOs') is not None:
            self.asset_os = m.get('AssetOs')
        if m.get('AssetSource') is not None:
            self.asset_source = m.get('AssetSource')
        if m.get('AssetSourceInstanceId') is not None:
            self.asset_source_instance_id = m.get('AssetSourceInstanceId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('OperationTicketId') is not None:
            self.operation_ticket_id = m.get('OperationTicketId')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListOperationTicketsResponseBody(TeaModel):
    def __init__(
        self,
        operation_tickets: List[ListOperationTicketsResponseBodyOperationTickets] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.operation_tickets = operation_tickets
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.operation_tickets:
            for k in self.operation_tickets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperationTickets'] = []
        if self.operation_tickets is not None:
            for k in self.operation_tickets:
                result['OperationTickets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation_tickets = []
        if m.get('OperationTickets') is not None:
            for k in m.get('OperationTickets'):
                temp_model = ListOperationTicketsResponseBodyOperationTickets()
                self.operation_tickets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOperationTicketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOperationTicketsResponseBody = None,
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
            temp_model = ListOperationTicketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The region ID of the bastion host.
        self.region_id = region_id
        # The type of the resource.
        # 
        # Set the value to INSTANCE, which indicates that the resource is a bastion host.
        self.resource_type = resource_type

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(
        self,
        tag_count: int = None,
        tag_key: str = None,
    ):
        # The total number of tag keys.
        self.tag_count = tag_count
        # The name of the tag key.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tag_keys: List[ListTagKeysResponseBodyTagKeys] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of tags.
        self.tag_keys = tag_keys
        # The total number of tags returned.
        self.total_count = total_count

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

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
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
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
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagKeysResponseBody = None,
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The ID of the request.
        self.key = key
        # The type of the resource.
        # 
        # The returned value is INSTANCE, which indicates that the resource is a Bastionhost instance.
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The region ID of the Bastionhost instance.
        self.next_token = next_token
        # The ID of the instance.
        self.region_id = region_id
        # The value of the tag.
        self.resource_id = resource_id
        # The operation that you want to perform.
        # 
        # Set the value to **ListTagResources**.
        self.resource_type = resource_type
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        # Queries the tags bound to one or more Bastionhost instances.
        self.next_token = next_token
        # ListTagResources
        self.request_id = request_id
        # 58928
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_group_name: str = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class ListUserGroupsResponseBodyUserGroups(TeaModel):
    def __init__(
        self,
        comment: str = None,
        member_count: int = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        self.comment = comment
        self.member_count = member_count
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class ListUserGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        user_groups: List[ListUserGroupsResponseBodyUserGroups] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.user_groups = user_groups

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
        status_code: int = None,
        body: ListUserGroupsResponseBody = None,
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
            temp_model = ListUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserPublicKeysRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The ID of the bastion host on which you want to query all public keys of the user.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.\
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The region ID of the bastion host on which you want to query all public keys of the user.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user whose public keys you want to query.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserPublicKeysResponseBodyPublicKeys(TeaModel):
    def __init__(
        self,
        comment: str = None,
        finger_print: str = None,
        public_key_id: str = None,
        public_key_name: str = None,
        user_id: str = None,
    ):
        # The description of the public key.
        self.comment = comment
        # The fingerprint of the public key.
        self.finger_print = finger_print
        # The ID of the public key.
        self.public_key_id = public_key_id
        # The name of the public key.
        self.public_key_name = public_key_name
        # The ID of the user to which the public key belongs.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.finger_print is not None:
            result['FingerPrint'] = self.finger_print
        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id
        if self.public_key_name is not None:
            result['PublicKeyName'] = self.public_key_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('FingerPrint') is not None:
            self.finger_print = m.get('FingerPrint')
        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')
        if m.get('PublicKeyName') is not None:
            self.public_key_name = m.get('PublicKeyName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserPublicKeysResponseBody(TeaModel):
    def __init__(
        self,
        public_keys: List[ListUserPublicKeysResponseBodyPublicKeys] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the public keys of the user.
        self.public_keys = public_keys
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of public keys.
        self.total_count = total_count

    def validate(self):
        if self.public_keys:
            for k in self.public_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PublicKeys'] = []
        if self.public_keys is not None:
            for k in self.public_keys:
                result['PublicKeys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.public_keys = []
        if m.get('PublicKeys') is not None:
            for k in m.get('PublicKeys'):
                temp_model = ListUserPublicKeysResponseBodyPublicKeys()
                self.public_keys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserPublicKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserPublicKeysResponseBody = None,
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
            temp_model = ListUserPublicKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        instance_id: str = None,
        mobile: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        source: str = None,
        source_user_id: str = None,
        user_group_id: str = None,
        user_name: str = None,
        user_state: str = None,
    ):
        # The display name of the user to be queried. Only exact match is supported.
        self.display_name = display_name
        # The ID of the Bastionhost instance to which the users to be queried belong.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.instance_id = instance_id
        # The mobile number of the user to be queried. Only exact match is supported.
        self.mobile = mobile
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # The value of the PageSize parameter must not exceed 100. By default, the number of entries on each page is 20. If you do not set the PageSize parameter, 20 entries are returned per page by default.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The region ID of the Bastionhost instance to which the users to be queried belong.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The source of the user to be queried. Valid values:
        # 
        # *   **Local**: a local user
        # *   **Ram**: a RAM user
        self.source = source
        # The unique ID of the user to be queried. Only exact match is supported.
        # 
        # >  This parameter uniquely identifies a RAM user of the Bastionhost instance. This parameter takes effect only when the **Source** parameter is set to **Ram**. You can call the [ListUsers](~~28684~~) operation to obtain the unique ID of the user from the **UserId** response parameter.
        self.source_user_id = source_user_id
        # The ID of the user group to be queried.
        # 
        # >  You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id
        # The logon name of the user to be queried. Only exact match is supported.
        self.user_name = user_name
        # The status of the user to be queried. Valid values:
        # 
        # *   **Normal**: The user can access the Bastionhost instance.
        # *   **Frozen**: The user is locked and cannot access the Bastionhost instance.
        # *   **Expired**: The user has expired and cannot access the Bastionhost instance.
        self.user_state = user_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_state is not None:
            result['UserState'] = self.user_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        comment: str = None,
        display_name: str = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        email: str = None,
        language: str = None,
        language_status: str = None,
        mobile: str = None,
        mobile_country_code: str = None,
        need_reset_password: bool = None,
        source: str = None,
        source_user_id: str = None,
        two_factor_methods: List[str] = None,
        two_factor_status: str = None,
        user_id: str = None,
        user_name: str = None,
        user_state: List[str] = None,
    ):
        # The description of the user.
        self.comment = comment
        # The display name of the user.
        self.display_name = display_name
        # The end of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time
        # The beginning of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time
        # The email address of the user.
        self.email = email
        self.language = language
        self.language_status = language_status
        # The mobile number of the user.
        self.mobile = mobile
        # The country where the mobile number of the user is registered. Valid values:
        # 
        # *   **CN**: the Chinese mainland, whose country calling code is +86
        # *   **HK**: Hong Kong (China), whose country calling code is +852
        # *   **MO**: Macau (China), whose country calling code is +853
        # *   **TW**: Taiwan (China), whose country calling code is +886
        # *   **RU**: Russia, whose country calling code is +7
        # *   **SG**: Singapore, whose country calling code is +65
        # *   **MY**: Malaysia, whose country calling code is +60
        # *   **ID**: Indonesia, whose country calling code is +62
        # *   **DE**: Germany, whose country calling code is +49
        # *   **AU**: Australia, whose country calling code is +61
        # *   **US**: United States, whose country calling code is +1
        # *   **AE**: United Arab Emirates, whose country calling code is +971
        # *   **JP**: Japan, whose country calling code is +81
        # *   **GB**: United Kingdom, whose country calling code is +44
        # *   **IN**: India, whose country calling code is +91
        # *   **KR**: South Korea, whose country calling code is +82
        # *   **PH**: Philippines, whose country calling code is +63
        # *   **CH**: Switzerland, whose country calling code is +41
        # *   **SE**: Sweden, whose country calling code is +46
        self.mobile_country_code = mobile_country_code
        # Specifies whether password reset is required upon the next logon. Valid values:
        # 
        # - true: yes
        # - false: no
        self.need_reset_password = need_reset_password
        # The source of the user. Valid values:
        # 
        # *   **Local**: a local user
        # *   **Ram**: a RAM user
        self.source = source
        # The unique ID of the user.
        # 
        # >  This parameter uniquely identifies a RAM user of the Bastionhost instance. A value is returned for this parameter if the **Source** parameter is set to **Ram**. No value is returned for this parameter if the **Source** parameter is set to **Local**.
        self.source_user_id = source_user_id
        # The two-factor authentication method.
        self.two_factor_methods = two_factor_methods
        # The two-factor authentication status of the user. Valid values:
        # 
        # *   **Global:** follows the global settings
        # *   **Disable:** disables two-factor authentication
        # *   **Enable:** enable two-factor authentication and follows settings of the single user
        self.two_factor_status = two_factor_status
        # The ID of the user.
        self.user_id = user_id
        # The logon name of the user.
        self.user_name = user_name
        # The statuses of the user.
        self.user_state = user_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.email is not None:
            result['Email'] = self.email
        if self.language is not None:
            result['Language'] = self.language
        if self.language_status is not None:
            result['LanguageStatus'] = self.language_status
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.need_reset_password is not None:
            result['NeedResetPassword'] = self.need_reset_password
        if self.source is not None:
            result['Source'] = self.source
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        if self.two_factor_status is not None:
            result['TwoFactorStatus'] = self.two_factor_status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_state is not None:
            result['UserState'] = self.user_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageStatus') is not None:
            self.language_status = m.get('LanguageStatus')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('NeedResetPassword') is not None:
            self.need_reset_password = m.get('NeedResetPassword')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        if m.get('TwoFactorStatus') is not None:
            self.two_factor_status = m.get('TwoFactorStatus')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        users: List[ListUsersResponseBodyUsers] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of users that were queried.
        self.total_count = total_count
        # The list of users that were queried.
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
        status_code: int = None,
        body: ListUsersResponseBody = None,
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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockUsersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        user_ids: str = None,
    ):
        # The ID of the bastion host to which the users to be locked belong.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host to which the users to be locked belong.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user to be locked. The value is a JSON string. You can add up to 100 user IDs. If you specify multiple IDs, separate the IDs with commas (,).
        # 
        # > You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        code: str = None,
        message: str = None,
        user_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # 
        # *   **UNEXPECTED**: An unknown error occurred.
        # 
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # 
        # >Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        # >Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # This parameter is deprecated.
        self.message = message
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class LockUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[LockUsersResponseBodyResults] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: LockUsersResponseBody = None,
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
            temp_model = LockUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        host_id: str = None,
        host_name: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        instance_id: str = None,
        network_domain_id: str = None,
        ostype: str = None,
        region_id: str = None,
    ):
        # The new description of the host. The description can be up to 500 characters in length.
        self.comment = comment
        # The ID of the host.
        # 
        # > You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.host_id = host_id
        # The new name of the host. The name can be up to 128 characters.
        self.host_name = host_name
        # The new internal endpoint of the host. You can set this parameter to a domain name or an IP address.
        self.host_private_address = host_private_address
        # The new public endpoint of the host. You can set this parameter to a domain name or an IP address.
        self.host_public_address = host_public_address
        # The ID of the bastion host on which you want to modify the information about the host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The ID of the new network domain to which the host belongs.
        self.network_domain_id = network_domain_id
        # The new operating system of the host. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.ostype = ostype
        # The region ID of the bastion host on which you want to modify the information about the host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyHostResponseBody = None,
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
            temp_model = ModifyHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostAccountRequest(TeaModel):
    def __init__(
        self,
        host_account_id: str = None,
        host_account_name: str = None,
        host_share_key_id: str = None,
        instance_id: str = None,
        pass_phrase: str = None,
        password: str = None,
        private_key: str = None,
        region_id: str = None,
    ):
        # The ID of the host account whose information you want to modify.
        # 
        # > You can call the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.host_account_id = host_account_id
        # The new name of the host account. The name can be up to 128 characters in length.
        self.host_account_name = host_account_name
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The ID of the bastion host in which you want to modify the information about the host account.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The passphrase of the new private key for the host account.
        # 
        # > This parameter takes effect only when the protocol of the host is set to SSH. If the protocol of the host is set to RDP, this parameter is not required.
        self.pass_phrase = pass_phrase
        # The new password of the host account.
        self.password = password
        # The new private key of the host account. The value is a Base64-encoded string.
        # 
        # > This parameter takes effect only when the protocol of the host is set to SSH. If the protocol of the host is set to RDP, this parameter is not required. You can call the [GetHostAccount](~~204391~~) operation to query the protocol used by the host. You can configure a password and a private key for the host account at the same time. If both a password and a private key are configured for the host account, Bastionhost preferentially uses the private key for logon.
        self.private_key = private_key
        # The region ID of the bastion host in which you want to query the details of the host account.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase
        if self.password is not None:
            result['Password'] = self.password
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyHostAccountResponseBody = None,
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
            temp_model = ModifyHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostGroupRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The new name of the host group. The name can be up to 128 characters in length.
        self.comment = comment
        # The region ID of the Bastionhost instance where you want to modify the information of the host group.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.host_group_id = host_group_id
        # The ID of the host group that you want to modify.
        # 
        # >  You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_name = host_group_name
        # The ID of the request.
        self.instance_id = instance_id
        # The ID of the Bastionhost instance where you want to modify the information of the host group.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyHostGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyHostGroupResponseBody = None,
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
            temp_model = ModifyHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostShareKeyRequest(TeaModel):
    def __init__(
        self,
        host_share_key_id: str = None,
        host_share_key_name: str = None,
        instance_id: str = None,
        pass_phrase: str = None,
        private_key: str = None,
        region_id: str = None,
    ):
        # The ID of the shared key whose information you want to modify.
        self.host_share_key_id = host_share_key_id
        # The name of the shared key.
        self.host_share_key_name = host_share_key_name
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The passphrase of the private key. The value is a Base64-encoded string.
        self.pass_phrase = pass_phrase
        # The private key. The value is a Base64-encoded string.
        self.private_key = private_key
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostShareKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class ModifyHostShareKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyHostShareKeyResponseBody = None,
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
            temp_model = ModifyHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostsActiveAddressTypeRequest(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        host_ids: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The new portal type of the host. Valid values:
        # 
        # *   **Public**: public portal
        # *   **Private**: internal portal
        self.active_address_type = active_address_type
        # The ID of the host for which you want to change the portal type. The value is a JSON string. You can add up to 100 host IDs.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.host_ids = host_ids
        # The ID of the bastion host for which you want to change the portal type of the host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host for which you want to change the portal type of the host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostsActiveAddressTypeResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_id: str = None,
        message: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The ID of the host.
        self.host_id = host_id
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ModifyHostsActiveAddressTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[ModifyHostsActiveAddressTypeResponseBodyResults] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ModifyHostsActiveAddressTypeResponseBody = None,
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
            temp_model = ModifyHostsActiveAddressTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostsPortRequest(TeaModel):
    def __init__(
        self,
        host_ids: str = None,
        instance_id: str = None,
        port: str = None,
        protocol_name: str = None,
        region_id: str = None,
    ):
        # The ID of the host for which you want to change the port. The value is a JSON string. You can add up to 100 host IDs. If you specify multiple IDs, separate the IDs with commas (,).
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the IDs of hosts.
        self.host_ids = host_ids
        # The ID of the bastion host for which you want to change the port of the host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The new port of the host. The port number must be an integer. Valid values: 22 to 65535.
        self.port = port
        # The protocol that is used to connect to the host. Valid values:
        # 
        # *   **SSH**\
        # *   **RDP**\
        self.protocol_name = protocol_name
        # The region ID of the bastion host for which you want to change the port of the host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostsPortResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_id: str = None,
        message: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        #     > Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        #     > Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT\_AlREADY\_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The ID of the host.
        self.host_id = host_id
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ModifyHostsPortResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[ModifyHostsPortResponseBodyResults] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ModifyHostsPortResponseBody = None,
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
            temp_model = ModifyHostsPortResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceADAuthServerRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        base_dn: str = None,
        domain: str = None,
        email_mapping: str = None,
        filter: str = None,
        instance_id: str = None,
        is_ssl: str = None,
        mobile_mapping: str = None,
        name_mapping: str = None,
        password: str = None,
        port: str = None,
        region_id: str = None,
        server: str = None,
        standby_server: str = None,
    ):
        # The username of the account that is used for the AD server.
        self.account = account
        # The Base distinguished name (DN).
        self.base_dn = base_dn
        # The domain on the AD server.
        self.domain = domain
        # The field that is used to indicate the email address of a user on the AD server.
        self.email_mapping = email_mapping
        # The condition that is used to filter users.
        self.filter = filter
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # Specifies whether to support SSL. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.is_ssl = is_ssl
        # The field that is used to indicate the mobile phone number of a user on the AD server.
        self.mobile_mapping = mobile_mapping
        # The field that is used to indicate the name of a user on the AD server.
        self.name_mapping = name_mapping
        # The password of the account that is used for the AD server.
        self.password = password
        # The port that is used to access the AD server.
        self.port = port
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The address of the AD server.
        self.server = server
        # The address of the secondary AD server.
        self.standby_server = standby_server

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.email_mapping is not None:
            result['EmailMapping'] = self.email_mapping
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl
        if self.mobile_mapping is not None:
            result['MobileMapping'] = self.mobile_mapping
        if self.name_mapping is not None:
            result['NameMapping'] = self.name_mapping
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server is not None:
            result['Server'] = self.server
        if self.standby_server is not None:
            result['StandbyServer'] = self.standby_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EmailMapping') is not None:
            self.email_mapping = m.get('EmailMapping')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')
        if m.get('MobileMapping') is not None:
            self.mobile_mapping = m.get('MobileMapping')
        if m.get('NameMapping') is not None:
            self.name_mapping = m.get('NameMapping')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('StandbyServer') is not None:
            self.standby_server = m.get('StandbyServer')
        return self


class ModifyInstanceADAuthServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class ModifyInstanceADAuthServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceADAuthServerResponseBody = None,
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
            temp_model = ModifyInstanceADAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The description of the bastion host.
        # 
        # > The description can contain only letters, digits, underscores (\_), and hyphens (-). The description can be up to 30 characters in length.
        self.description = description
        # The ID of the bastion host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceAttributeResponseBody = None,
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
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceLDAPAuthServerRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        base_dn: str = None,
        email_mapping: str = None,
        filter: str = None,
        instance_id: str = None,
        is_ssl: str = None,
        login_name_mapping: str = None,
        mobile_mapping: str = None,
        name_mapping: str = None,
        password: str = None,
        port: str = None,
        region_id: str = None,
        server: str = None,
        standby_server: str = None,
    ):
        # The username of the account that is used for the LDAP server.
        self.account = account
        # The Base distinguished name (DN).
        self.base_dn = base_dn
        # The field that is used to indicate the email address of a user on the LDAP server.
        self.email_mapping = email_mapping
        # The condition that is used to filter users.
        self.filter = filter
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # Specifies whether to support SSL. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_ssl = is_ssl
        # The field that is used to indicate the logon name of a user on the LDAP server.
        self.login_name_mapping = login_name_mapping
        # The field that is used to indicate the mobile phone number of a user on the LDAP server.
        self.mobile_mapping = mobile_mapping
        # The field that is used to indicate the name of a user on the LDAP server.
        self.name_mapping = name_mapping
        # The password of the account that is used for the LDAP server. You must configure a password when you configure LDAP authentication. If you leave this parameter empty when you modify the settings of LDAP authentication, the current password is used.
        self.password = password
        # The port that is used to access the LDAP server.
        self.port = port
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The address of the LDAP server.
        self.server = server
        # The address of the secondary LDAP server.
        self.standby_server = standby_server

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn
        if self.email_mapping is not None:
            result['EmailMapping'] = self.email_mapping
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl
        if self.login_name_mapping is not None:
            result['LoginNameMapping'] = self.login_name_mapping
        if self.mobile_mapping is not None:
            result['MobileMapping'] = self.mobile_mapping
        if self.name_mapping is not None:
            result['NameMapping'] = self.name_mapping
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server is not None:
            result['Server'] = self.server
        if self.standby_server is not None:
            result['StandbyServer'] = self.standby_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')
        if m.get('EmailMapping') is not None:
            self.email_mapping = m.get('EmailMapping')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')
        if m.get('LoginNameMapping') is not None:
            self.login_name_mapping = m.get('LoginNameMapping')
        if m.get('MobileMapping') is not None:
            self.mobile_mapping = m.get('MobileMapping')
        if m.get('NameMapping') is not None:
            self.name_mapping = m.get('NameMapping')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('StandbyServer') is not None:
            self.standby_server = m.get('StandbyServer')
        return self


class ModifyInstanceLDAPAuthServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class ModifyInstanceLDAPAuthServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceLDAPAuthServerResponseBody = None,
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
            temp_model = ModifyInstanceLDAPAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceTwoFactorRequest(TeaModel):
    def __init__(
        self,
        enable_two_factor: str = None,
        instance_id: str = None,
        region_id: str = None,
        skip_two_factor_time: str = None,
        two_factor_methods: str = None,
    ):
        # Specifies whether to enable two-factor authentication. Valid values:
        # 
        # *   **true**: enables two-factor authentication.
        # *   **false**: disables two-factor authentication.
        self.enable_two_factor = enable_two_factor
        # The ID of the bastion host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.skip_two_factor_time = skip_two_factor_time
        # One or more methods that are used to send a verification code if two-factor authentication is enabled. If you set the EnableTwoFactor parameter to true, you must specify at least one method. Valid values:
        # 
        # *   **sms**: text message
        # *   **email**: email
        # *   **dingtalk**: Notice in DingTalk
        self.two_factor_methods = two_factor_methods

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_two_factor is not None:
            result['EnableTwoFactor'] = self.enable_two_factor
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.skip_two_factor_time is not None:
            result['SkipTwoFactorTime'] = self.skip_two_factor_time
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTwoFactor') is not None:
            self.enable_two_factor = m.get('EnableTwoFactor')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SkipTwoFactorTime') is not None:
            self.skip_two_factor_time = m.get('SkipTwoFactorTime')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        return self


class ModifyInstanceTwoFactorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The duration within which two-factor authentication is not required after a local user passes two-factor authentication. Valid values: 0 to 168. Unit: hours. If you set this parameter to 0, the local user must pass two-factor authentication every time the local user logs on to the bastion host.
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


class ModifyInstanceTwoFactorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceTwoFactorResponseBody = None,
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
            temp_model = ModifyInstanceTwoFactorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        display_name: str = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        email: str = None,
        instance_id: str = None,
        language: str = None,
        language_status: str = None,
        mobile: str = None,
        mobile_country_code: str = None,
        need_reset_password: bool = None,
        password: str = None,
        region_id: str = None,
        two_factor_methods: str = None,
        two_factor_status: str = None,
        user_id: str = None,
    ):
        # The new description of the user. The description can be up to 500 characters in length.
        self.comment = comment
        # The new display name of the user. This display name can be up to 128 characters in length.
        self.display_name = display_name
        # The end of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time
        # The beginning of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time
        # The new email address of the user.
        # 
        # > This parameter is required when the TwoFactorStatus parameter is set to Enable and the TwoFactorMethods parameter is set to email.
        self.email = email
        # The ID of the bastion host where you want to modify user information.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        self.language = language
        self.language_status = language_status
        # The new mobile number of the user.
        # 
        # > This parameter is required when the TwoFactorStatus parameter is set to Enable and the TwoFactorMethods parameter is set to sms or dingtalk.
        self.mobile = mobile
        # The country where the new mobile number of the user is registered. Valid values:
        # 
        # *   **CN:** the Chinese mainland, whose country calling code is +86
        # *   **HK:** Hong Kong (China), whose country calling code is +852
        # *   **MO:** Macao (China), whose country calling code is +853
        # *   **TW:** Taiwan (China), whose country calling code is +886
        # *   **RU:** Russia, whose country calling code is +7
        # *   **SG:** Singapore, whose country calling code is +65
        # *   **MY:** Malaysia, whose country calling code is +60
        # *   **ID:** Indonesia, whose country calling code is +62
        # *   **DE:** Germany, whose country calling code is +49
        # *   **AU:** Australia, whose country calling code is +61
        # *   **US:** US, whose country calling code is +1
        # *   **AE:** United Arab Emirates, whose country calling code is +971
        # *   **JP:** Japan, whose country calling code is +81
        # *   **GB:** UK, whose country calling code is +44
        # *   **IN:** India, whose country calling code is +91
        # *   **KR:** Republic of Korea, whose country calling code is +82
        # *   **PH:** Philippines, whose country calling code is +63
        # *   **CH:** Switzerland, whose country calling code is +41
        # *   **SE:** Sweden, whose country calling code is +46
        # *   **SA:** Saudi Arabia, whose country calling code is +966
        self.mobile_country_code = mobile_country_code
        # Specifies whether password reset is required upon the next logon. Valid values:
        # 
        # - true: yes
        # - false: no
        self.need_reset_password = need_reset_password
        # The new password of the user. The password must be 8 to 128 characters in length and must contain lowercase letters, uppercase letters, digits, and special characters.
        self.password = password
        # The region ID of the bastion host where you want to modify user information.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The two-factor authentication method. You can select only one method. Valid values:
        # 
        # *   **sms:** text message
        # *   **email:** email
        # *   **dingtalk:** DingTalk
        # *   **totp OTP:** time-based one-time password (TOTP) app
        # 
        # > *   When the TwoFactorStatus parameter is set to Enable, you must specify one of the preceding values.
        self.two_factor_methods = two_factor_methods
        # The two-factor authentication status of the user. Valid values:
        # 
        # *   **Global:** follows the global settings
        # *   **Disable:** disables two-factor authentication
        # *   **Enable:** enable two-factor authentication and follows settings of the single user
        self.two_factor_status = two_factor_status
        # The ID of the user whose information you want to modify.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.email is not None:
            result['Email'] = self.email
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.language is not None:
            result['Language'] = self.language
        if self.language_status is not None:
            result['LanguageStatus'] = self.language_status
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.need_reset_password is not None:
            result['NeedResetPassword'] = self.need_reset_password
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        if self.two_factor_status is not None:
            result['TwoFactorStatus'] = self.two_factor_status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageStatus') is not None:
            self.language_status = m.get('LanguageStatus')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('NeedResetPassword') is not None:
            self.need_reset_password = m.get('NeedResetPassword')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        if m.get('TwoFactorStatus') is not None:
            self.two_factor_status = m.get('TwoFactorStatus')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ModifyUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class ModifyUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyUserResponseBody = None,
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
            temp_model = ModifyUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserGroupRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        # The new description of the user group. The description can be up to 500 characters in length.
        self.comment = comment
        # The ID of the bastion host in which you want to modify the information about the user group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host in which you want to modify the information about the user group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user group that you want to modify.
        # 
        # > You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id
        # The new name of the user group. This name can be up to 128 characters in length.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class ModifyUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyUserGroupResponseBody = None,
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
            temp_model = ModifyUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The region ID of the bastion host.
        self.region_id = region_id
        # The ID of the resource group to which the bastion host is moved.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the resource group ID of the bastion host.
        self.resource_group_id = resource_group_id
        # The ID of the bastion host for which you want to change the resource group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.resource_id = resource_id
        # The type of the resource. Set the value to **INSTANCE**, which indicates that the resource is a bastion host.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveResourceGroupResponseBody = None,
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectApproveCommandRequest(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.command_id = command_id
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RejectApproveCommandResponseBody(TeaModel):
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


class RejectApproveCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RejectApproveCommandResponseBody = None,
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
            temp_model = RejectApproveCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectOperationTicketRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        operation_ticket_id: str = None,
        region_id: str = None,
    ):
        # The ID of the bastion host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The ID of the O\&M application that you want to reject. You can call the ListOperationTickets operation to query the IDs of all O\&M applications that require review.
        self.operation_ticket_id = operation_ticket_id
        # The region ID of the bastion host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.operation_ticket_id is not None:
            result['OperationTicketId'] = self.operation_ticket_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OperationTicketId') is not None:
            self.operation_ticket_id = m.get('OperationTicketId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RejectOperationTicketResponseBody(TeaModel):
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


class RejectOperationTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RejectOperationTicketResponseBody = None,
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
            temp_model = RejectOperationTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveHostsFromGroupRequest(TeaModel):
    def __init__(
        self,
        host_group_id: str = None,
        host_ids: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the host group from which you want to remove hosts.
        # 
        # >  You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_id = host_group_id
        # The ID of the host that you want to remove from the host group. The value is a JSON string. You can add up to 100 host IDs.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the IDs of hosts.
        self.host_ids = host_ids
        # The ID of the bastion host for which you want to remove hosts from the host group.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host for which you want to remove hosts from the host group.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RemoveHostsFromGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_group_id: str = None,
        host_id: str = None,
        message: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The ID of the host group.
        self.host_group_id = host_group_id
        # The ID of the host.
        self.host_id = host_id
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveHostsFromGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[RemoveHostsFromGroupResponseBodyResults] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: RemoveHostsFromGroupResponseBody = None,
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
            temp_model = RemoveHostsFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUsersFromGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
        user_ids: str = None,
    ):
        # The ID of the bastion host for which you want to remove users from the user group.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host for which you want to remove users from the user group.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user group from which you want to remove users.
        # 
        # >  You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id
        # The ID of the user who you want to remove. The value is a JSON string. You can add up to 100 user IDs. If you specify multiple IDs, separate the IDs with commas (,).
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the IDs of users.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        code: str = None,
        message: str = None,
        user_group_id: str = None,
        user_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # 
        # *   **UNEXPECTED**: An unknown error occurred.
        # 
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # 
        # > Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        # > Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # This parameter is deprecated.
        self.message = message
        # The ID of the group.
        self.user_group_id = user_group_id
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RemoveUsersFromGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[RemoveUsersFromGroupResponseBodyResults] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: RemoveUsersFromGroupResponseBody = None,
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
            temp_model = RemoveUsersFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetHostAccountCredentialRequest(TeaModel):
    def __init__(
        self,
        credential_type: str = None,
        host_account_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The type of the logon credential that you want to delete. Valid values:
        # 
        # *   **Password**\
        # *   **PrivateKey**\
        self.credential_type = credential_type
        # The ID of the host account for which the logon credential is to be deleted.
        # 
        # >  You can call the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.host_account_id = host_account_id
        # The ID of the bastion host from which you want to delete the logon credential for the host account.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host from which you want to delete the logon credential for the host account.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResetHostAccountCredentialResponseBody(TeaModel):
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


class ResetHostAccountCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetHostAccountCredentialResponseBody = None,
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
            temp_model = ResetHostAccountCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        security_group_ids: List[str] = None,
        vswitch_id: str = None,
    ):
        # The ID of the bastion host that you want to enable.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host.
        self.region_id = region_id
        # An array consisting of the IDs of security groups to which the bastion host is added.
        self.security_group_ids = security_group_ids
        # The ID of the vSwitch to which the bastion host belongs.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        # The ID of the bastion host that you enable.
        self.instance_id = instance_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartInstanceResponseBody = None,
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. Valid values of N: 1 to 20.
        # 
        # > 
        # 
        # *   The value can be up to 128 characters in length but cannot be an empty string.
        # 
        # *   The value cannot start with **aliyun** or **acs:**. The value cannot contain **http://** or **https://**.
        self.key = key
        # The value of tag N.\
        # Valid values of N: 1 to 20.
        # 
        # > 
        # 
        # *   The value can be up to 128 characters in length or an empty string.
        # 
        # *   The value cannot start with **aliyun** or **acs:**. The value cannot contain **http://** or **https://**.
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The region ID of the bastion hosts to which you want to create and add tags.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # An array that consists of IDs of bastion hosts.
        # 
        # Valid values: 1 to 20.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query IDs of bastion hosts.
        self.resource_id = resource_id
        # The type of the resource.
        # 
        # Set the value to **INSTANCE**, which indicates that the resource is a bastion host.
        self.resource_type = resource_type
        # An array that consists of tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
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
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockUsersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        user_ids: str = None,
    ):
        # The ID of the bastion host to which the users to be unlocked belong.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host to which the users to be unlocked belong.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user that you want to unlock. The value is a JSON string. You can add up to 100 user IDs. If you specify multiple IDs, separate the IDs with commas (,).
        # 
        # > You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        code: str = None,
        message: str = None,
        user_id: str = None,
    ):
        # The result of the call. Valid values:
        # 
        # *   **OK**: The call was successful.
        # 
        # *   **UNEXPECTED**: An unknown error occurred.
        # 
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # 
        #     **\
        # 
        #     **Note**Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        #     **\
        # 
        #     **Note**Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # This parameter is deprecated.
        self.message = message
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UnlockUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[UnlockUsersResponseBodyResults] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of information about the result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: UnlockUsersResponseBody = None,
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
            temp_model = UnlockUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to delete all tags that are added to the bastion host.
        # 
        # *   If you specify TagKey.N, the value of this parameter can only be **false**, which indicates that only a specified tag is deleted.
        # *   If you do not specify TagKey.N and the value of this parameter is **true**, all tags are deleted. If you do not specify TagKey.N and the value of this parameter is **false**, no tags are deleted.
        self.all = all
        # The region ID of the bastion host to query.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # An array that consists of IDs of bastion hosts.
        # 
        # Valid values: 1 to 20.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.resource_id = resource_id
        # The type of the resource.
        # 
        # Set the value to **INSTANCE**, which indicates that the resource is a bastion host.
        self.resource_type = resource_type
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


