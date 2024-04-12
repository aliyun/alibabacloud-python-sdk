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


class AddDatabasesToGroupRequest(TeaModel):
    def __init__(
        self,
        database_ids: List[str] = None,
        host_group_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.database_ids = database_ids
        self.host_group_id = host_group_id
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_ids is not None:
            result['DatabaseIds'] = self.database_ids
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseIds') is not None:
            self.database_ids = m.get('DatabaseIds')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddDatabasesToGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_id: str = None,
        host_group_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.database_id = database_id
        self.host_group_id = host_group_id
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
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddDatabasesToGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AddDatabasesToGroupResponseBodyResults] = None,
    ):
        self.request_id = request_id
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
                temp_model = AddDatabasesToGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AddDatabasesToGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDatabasesToGroupResponseBody = None,
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
            temp_model = AddDatabasesToGroupResponseBody()
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


class AttachDatabaseAccountsToUserRequestDatabases(TeaModel):
    def __init__(
        self,
        database_account_ids: List[str] = None,
        database_id: str = None,
    ):
        self.database_account_ids = database_account_ids
        self.database_id = database_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_ids is not None:
            result['DatabaseAccountIds'] = self.database_account_ids
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountIds') is not None:
            self.database_account_ids = m.get('DatabaseAccountIds')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        return self


class AttachDatabaseAccountsToUserRequest(TeaModel):
    def __init__(
        self,
        databases: List[AttachDatabaseAccountsToUserRequestDatabases] = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        self.databases = databases
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_id = user_id

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = AttachDatabaseAccountsToUserRequestDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AttachDatabaseAccountsToUserResponseBodyResultsDatabaseAccounts(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_account_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.database_account_id = database_account_id
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
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachDatabaseAccountsToUserResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_accounts: List[AttachDatabaseAccountsToUserResponseBodyResultsDatabaseAccounts] = None,
        database_id: str = None,
        message: str = None,
        user_id: str = None,
    ):
        self.code = code
        self.database_accounts = database_accounts
        self.database_id = database_id
        self.message = message
        self.user_id = user_id

    def validate(self):
        if self.database_accounts:
            for k in self.database_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DatabaseAccounts'] = []
        if self.database_accounts is not None:
            for k in self.database_accounts:
                result['DatabaseAccounts'].append(k.to_map() if k else None)
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.database_accounts = []
        if m.get('DatabaseAccounts') is not None:
            for k in m.get('DatabaseAccounts'):
                temp_model = AttachDatabaseAccountsToUserResponseBodyResultsDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k))
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AttachDatabaseAccountsToUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AttachDatabaseAccountsToUserResponseBodyResults] = None,
    ):
        self.request_id = request_id
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
                temp_model = AttachDatabaseAccountsToUserResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AttachDatabaseAccountsToUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachDatabaseAccountsToUserResponseBody = None,
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
            temp_model = AttachDatabaseAccountsToUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachDatabaseAccountsToUserGroupRequestDatabases(TeaModel):
    def __init__(
        self,
        database_account_ids: List[str] = None,
        database_id: str = None,
    ):
        self.database_account_ids = database_account_ids
        self.database_id = database_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_ids is not None:
            result['DatabaseAccountIds'] = self.database_account_ids
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountIds') is not None:
            self.database_account_ids = m.get('DatabaseAccountIds')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        return self


class AttachDatabaseAccountsToUserGroupRequest(TeaModel):
    def __init__(
        self,
        databases: List[AttachDatabaseAccountsToUserGroupRequestDatabases] = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        self.databases = databases
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = AttachDatabaseAccountsToUserGroupRequestDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AttachDatabaseAccountsToUserGroupResponseBodyResultsDatabaseAccounts(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_account_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.database_account_id = database_account_id
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
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachDatabaseAccountsToUserGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_accounts: List[AttachDatabaseAccountsToUserGroupResponseBodyResultsDatabaseAccounts] = None,
        database_id: str = None,
        message: str = None,
        user_group_id: str = None,
    ):
        self.code = code
        self.database_accounts = database_accounts
        self.database_id = database_id
        self.message = message
        self.user_group_id = user_group_id

    def validate(self):
        if self.database_accounts:
            for k in self.database_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DatabaseAccounts'] = []
        if self.database_accounts is not None:
            for k in self.database_accounts:
                result['DatabaseAccounts'].append(k.to_map() if k else None)
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.database_accounts = []
        if m.get('DatabaseAccounts') is not None:
            for k in m.get('DatabaseAccounts'):
                temp_model = AttachDatabaseAccountsToUserGroupResponseBodyResultsDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k))
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AttachDatabaseAccountsToUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AttachDatabaseAccountsToUserGroupResponseBodyResults] = None,
    ):
        self.request_id = request_id
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
                temp_model = AttachDatabaseAccountsToUserGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AttachDatabaseAccountsToUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachDatabaseAccountsToUserGroupResponseBody = None,
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
            temp_model = AttachDatabaseAccountsToUserGroupResponseBody()
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
        # The ID of the bastion host for which you want to configure a whitelist of public IP addresses.
        self.instance_id = instance_id
        # The region ID of the bastion host.
        self.region_id = region_id
        # The public IP addresses that you want to add to the whitelist.
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
        # The ID of the bastion host for which a whitelist of public IP addresses is configured.
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


class CreateDatabaseRequest(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        database_name: str = None,
        database_port: int = None,
        database_private_address: str = None,
        database_public_address: str = None,
        database_type: str = None,
        instance_id: str = None,
        network_domain_id: str = None,
        polar_dbendpoint_type: str = None,
        region_id: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_region_id: str = None,
    ):
        self.active_address_type = active_address_type
        self.comment = comment
        self.database_name = database_name
        self.database_port = database_port
        self.database_private_address = database_private_address
        self.database_public_address = database_public_address
        self.database_type = database_type
        self.instance_id = instance_id
        self.network_domain_id = network_domain_id
        self.polar_dbendpoint_type = polar_dbendpoint_type
        self.region_id = region_id
        self.source = source
        self.source_instance_id = source_instance_id
        self.source_instance_region_id = source_instance_region_id

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
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_port is not None:
            result['DatabasePort'] = self.database_port
        if self.database_private_address is not None:
            result['DatabasePrivateAddress'] = self.database_private_address
        if self.database_public_address is not None:
            result['DatabasePublicAddress'] = self.database_public_address
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.polar_dbendpoint_type is not None:
            result['PolarDBEndpointType'] = self.polar_dbendpoint_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_instance_region_id is not None:
            result['SourceInstanceRegionId'] = self.source_instance_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabasePort') is not None:
            self.database_port = m.get('DatabasePort')
        if m.get('DatabasePrivateAddress') is not None:
            self.database_private_address = m.get('DatabasePrivateAddress')
        if m.get('DatabasePublicAddress') is not None:
            self.database_public_address = m.get('DatabasePublicAddress')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('PolarDBEndpointType') is not None:
            self.polar_dbendpoint_type = m.get('PolarDBEndpointType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceInstanceRegionId') is not None:
            self.source_instance_region_id = m.get('SourceInstanceRegionId')
        return self


class CreateDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        request_id: str = None,
    ):
        self.database_id = database_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatabaseResponseBody = None,
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
            temp_model = CreateDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatabaseAccountRequest(TeaModel):
    def __init__(
        self,
        database_account_name: str = None,
        database_id: str = None,
        database_schema: str = None,
        instance_id: str = None,
        login_attribute: str = None,
        password: str = None,
        region_id: str = None,
    ):
        self.database_account_name = database_account_name
        self.database_id = database_id
        self.database_schema = database_schema
        self.instance_id = instance_id
        self.login_attribute = login_attribute
        self.password = password
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_schema is not None:
            result['DatabaseSchema'] = self.database_schema
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.login_attribute is not None:
            result['LoginAttribute'] = self.login_attribute
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseSchema') is not None:
            self.database_schema = m.get('DatabaseSchema')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LoginAttribute') is not None:
            self.login_attribute = m.get('LoginAttribute')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateDatabaseAccountResponseBody(TeaModel):
    def __init__(
        self,
        database_account_id: str = None,
        request_id: str = None,
    ):
        self.database_account_id = database_account_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatabaseAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatabaseAccountResponseBody = None,
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
            temp_model = CreateDatabaseAccountResponseBody()
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
        # The name of the host account.
        self.host_account_name = host_account_name
        # The ID of the host to which you want to add a host account.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.host_id = host_id
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The ID of the bastion host in which you want to add a host account to the host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The passphrase of the private key for the host account.
        # 
        # >  You can specify this parameter when the ProtocolName parameter is set to SSH. If the ProtocolName parameter is set to RDP, you do not need to specify this parameter.
        self.pass_phrase = pass_phrase
        # The password of the host account.
        self.password = password
        # The private key of the host account. The value is a Base64-encoded string.
        # 
        # >  This parameter takes effect only when the ProtocolName parameter is set to SSH. If the ProtocolName parameter is set to RDP, you do not need to specify this parameter. You can configure a password and a private key for the host account at the same time. If both a password and a private key are configured for the host account, Bastionhost preferentially uses the private key to log on to the host.
        self.private_key = private_key
        # The protocol of the host to which you want to add a host account.
        # 
        # Valid values:
        # 
        # *   SSH
        # *   RDP
        self.protocol_name = protocol_name
        # The region ID of the bastion host in which you want to add a host account to the host.
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
        # The operation that you want to perform. Set the value to **CreateHostAccount**.
        self.host_account_id = host_account_id
        # The ID of the request.
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


class CreateNetworkDomainRequestProxies(TeaModel):
    def __init__(
        self,
        address: str = None,
        node_type: str = None,
        password: str = None,
        port: int = None,
        proxy_type: str = None,
        user: str = None,
    ):
        self.address = address
        self.node_type = node_type
        self.password = password
        self.port = port
        self.proxy_type = proxy_type
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class CreateNetworkDomainRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        network_domain_name: str = None,
        network_domain_type: str = None,
        proxies: List[CreateNetworkDomainRequestProxies] = None,
        region_id: str = None,
    ):
        self.comment = comment
        self.instance_id = instance_id
        self.network_domain_name = network_domain_name
        self.network_domain_type = network_domain_type
        self.proxies = proxies
        self.region_id = region_id

    def validate(self):
        if self.proxies:
            for k in self.proxies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_domain_name is not None:
            result['NetworkDomainName'] = self.network_domain_name
        if self.network_domain_type is not None:
            result['NetworkDomainType'] = self.network_domain_type
        result['Proxies'] = []
        if self.proxies is not None:
            for k in self.proxies:
                result['Proxies'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainName') is not None:
            self.network_domain_name = m.get('NetworkDomainName')
        if m.get('NetworkDomainType') is not None:
            self.network_domain_type = m.get('NetworkDomainType')
        self.proxies = []
        if m.get('Proxies') is not None:
            for k in m.get('Proxies'):
                temp_model = CreateNetworkDomainRequestProxies()
                self.proxies.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateNetworkDomainResponseBody(TeaModel):
    def __init__(
        self,
        network_domain_id: str = None,
        request_id: str = None,
    ):
        self.network_domain_id = network_domain_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNetworkDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNetworkDomainResponseBody = None,
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
            temp_model = CreateNetworkDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        policy_name: str = None,
        priority: str = None,
        region_id: str = None,
    ):
        self.comment = comment
        self.instance_id = instance_id
        self.policy_name = policy_name
        self.priority = priority
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
        request_id: str = None,
    ):
        self.policy_id = policy_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
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


class CreateRuleRequestDatabases(TeaModel):
    def __init__(
        self,
        database_account_ids: List[str] = None,
        database_id: str = None,
    ):
        self.database_account_ids = database_account_ids
        self.database_id = database_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_ids is not None:
            result['DatabaseAccountIds'] = self.database_account_ids
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountIds') is not None:
            self.database_account_ids = m.get('DatabaseAccountIds')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        return self


class CreateRuleRequestHostGroups(TeaModel):
    def __init__(
        self,
        host_account_names: List[str] = None,
        host_group_id: str = None,
    ):
        self.host_account_names = host_account_names
        self.host_group_id = host_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_names is not None:
            result['HostAccountNames'] = self.host_account_names
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountNames') is not None:
            self.host_account_names = m.get('HostAccountNames')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class CreateRuleRequestHosts(TeaModel):
    def __init__(
        self,
        host_account_ids: List[str] = None,
        host_id: str = None,
    ):
        self.host_account_ids = host_account_ids
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_ids is not None:
            result['HostAccountIds'] = self.host_account_ids
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountIds') is not None:
            self.host_account_ids = m.get('HostAccountIds')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class CreateRuleRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        databases: List[CreateRuleRequestDatabases] = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        host_groups: List[CreateRuleRequestHostGroups] = None,
        hosts: List[CreateRuleRequestHosts] = None,
        instance_id: str = None,
        region_id: str = None,
        rule_name: str = None,
        user_group_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        self.comment = comment
        self.databases = databases
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.host_groups = host_groups
        self.hosts = hosts
        self.instance_id = instance_id
        self.region_id = region_id
        self.rule_name = rule_name
        self.user_group_ids = user_group_ids
        self.user_ids = user_ids

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = CreateRuleRequestDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = CreateRuleRequestHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = CreateRuleRequestHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rule_id: str = None,
    ):
        self.request_id = request_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRuleResponseBody = None,
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
            temp_model = CreateRuleResponseBody()
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


class DeleteDatabaseRequest(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.database_id = database_id
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDatabaseResponseBody(TeaModel):
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


class DeleteDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatabaseResponseBody = None,
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
            temp_model = DeleteDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatabaseAccountRequest(TeaModel):
    def __init__(
        self,
        database_account_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.database_account_id = database_account_id
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDatabaseAccountResponseBody(TeaModel):
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


class DeleteDatabaseAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatabaseAccountResponseBody = None,
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
            temp_model = DeleteDatabaseAccountResponseBody()
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


class DeleteNetworkDomainRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        network_domain_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.network_domain_id = network_domain_id
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
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteNetworkDomainResponseBody(TeaModel):
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


class DeleteNetworkDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNetworkDomainResponseBody = None,
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
            temp_model = DeleteNetworkDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.policy_id = policy_id
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
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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


class DeleteRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        rule_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.rule_id = rule_id

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
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteRuleResponseBody(TeaModel):
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


class DeleteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRuleResponseBody = None,
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
            temp_model = DeleteRuleResponseBody()
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
        # The ID of the Bastionhost instance to which the users to be queried belong.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
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
        # The natural language in which responses are returned. Valid values:
        # 
        # *   **zh-CN**: Chinese. This is the default value.
        # *   **en-US**: English.
        # *   **ja**: Japanese.
        self.accept_language = accept_language
        # The ID of the region.
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
        # The name of the region.
        self.local_name = local_name
        # The endpoint of the region.
        self.region_endpoint = region_endpoint
        # The ID of the region.
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
        # The information about regions where you can create bastion hosts.
        self.regions = regions
        # The ID of request.
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


class DetachDatabaseAccountsFromUserRequestDatabases(TeaModel):
    def __init__(
        self,
        database_account_ids: List[str] = None,
        database_id: str = None,
    ):
        self.database_account_ids = database_account_ids
        self.database_id = database_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_ids is not None:
            result['DatabaseAccountIds'] = self.database_account_ids
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountIds') is not None:
            self.database_account_ids = m.get('DatabaseAccountIds')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        return self


class DetachDatabaseAccountsFromUserRequest(TeaModel):
    def __init__(
        self,
        databases: List[DetachDatabaseAccountsFromUserRequestDatabases] = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        self.databases = databases
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_id = user_id

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = DetachDatabaseAccountsFromUserRequestDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DetachDatabaseAccountsFromUserResponseBodyResultsDatabaseAccounts(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_account_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.database_account_id = database_account_id
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
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DetachDatabaseAccountsFromUserResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_accounts: List[DetachDatabaseAccountsFromUserResponseBodyResultsDatabaseAccounts] = None,
        database_id: str = None,
        message: str = None,
        user_id: str = None,
    ):
        self.code = code
        self.database_accounts = database_accounts
        self.database_id = database_id
        self.message = message
        self.user_id = user_id

    def validate(self):
        if self.database_accounts:
            for k in self.database_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DatabaseAccounts'] = []
        if self.database_accounts is not None:
            for k in self.database_accounts:
                result['DatabaseAccounts'].append(k.to_map() if k else None)
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.database_accounts = []
        if m.get('DatabaseAccounts') is not None:
            for k in m.get('DatabaseAccounts'):
                temp_model = DetachDatabaseAccountsFromUserResponseBodyResultsDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k))
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DetachDatabaseAccountsFromUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[DetachDatabaseAccountsFromUserResponseBodyResults] = None,
    ):
        self.request_id = request_id
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
                temp_model = DetachDatabaseAccountsFromUserResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetachDatabaseAccountsFromUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachDatabaseAccountsFromUserResponseBody = None,
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
            temp_model = DetachDatabaseAccountsFromUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachDatabaseAccountsFromUserGroupRequestDatabases(TeaModel):
    def __init__(
        self,
        database_account_ids: List[str] = None,
        database_id: str = None,
    ):
        self.database_account_ids = database_account_ids
        self.database_id = database_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_ids is not None:
            result['DatabaseAccountIds'] = self.database_account_ids
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountIds') is not None:
            self.database_account_ids = m.get('DatabaseAccountIds')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        return self


class DetachDatabaseAccountsFromUserGroupRequest(TeaModel):
    def __init__(
        self,
        databases: List[DetachDatabaseAccountsFromUserGroupRequestDatabases] = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        self.databases = databases
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = DetachDatabaseAccountsFromUserGroupRequestDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DetachDatabaseAccountsFromUserGroupResponseBodyResultsDatabaseAccounts(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_account_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.database_account_id = database_account_id
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
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DetachDatabaseAccountsFromUserGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_accounts: List[DetachDatabaseAccountsFromUserGroupResponseBodyResultsDatabaseAccounts] = None,
        database_id: str = None,
        message: str = None,
        user_group_id: str = None,
    ):
        self.code = code
        self.database_accounts = database_accounts
        self.database_id = database_id
        self.message = message
        self.user_group_id = user_group_id

    def validate(self):
        if self.database_accounts:
            for k in self.database_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DatabaseAccounts'] = []
        if self.database_accounts is not None:
            for k in self.database_accounts:
                result['DatabaseAccounts'].append(k.to_map() if k else None)
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.database_accounts = []
        if m.get('DatabaseAccounts') is not None:
            for k in m.get('DatabaseAccounts'):
                temp_model = DetachDatabaseAccountsFromUserGroupResponseBodyResultsDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k))
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DetachDatabaseAccountsFromUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[DetachDatabaseAccountsFromUserGroupResponseBodyResults] = None,
    ):
        self.request_id = request_id
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
                temp_model = DetachDatabaseAccountsFromUserGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetachDatabaseAccountsFromUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachDatabaseAccountsFromUserGroupResponseBody = None,
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
            temp_model = DetachDatabaseAccountsFromUserGroupResponseBody()
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


class DisableRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        rule_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.rule_id = rule_id

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
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DisableRuleResponseBody(TeaModel):
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


class DisableRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableRuleResponseBody = None,
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
            temp_model = DisableRuleResponseBody()
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


class EnableRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        rule_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.rule_id = rule_id

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
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class EnableRuleResponseBody(TeaModel):
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


class EnableRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableRuleResponseBody = None,
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
            temp_model = EnableRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAssetOperationTokenRequest(TeaModel):
    def __init__(
        self,
        asset_account_id: str = None,
        asset_account_name: str = None,
        asset_account_password: str = None,
        asset_account_protocol_name: str = None,
        asset_id: str = None,
        asset_type: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.asset_account_id = asset_account_id
        self.asset_account_name = asset_account_name
        self.asset_account_password = asset_account_password
        self.asset_account_protocol_name = asset_account_protocol_name
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_account_id is not None:
            result['AssetAccountId'] = self.asset_account_id
        if self.asset_account_name is not None:
            result['AssetAccountName'] = self.asset_account_name
        if self.asset_account_password is not None:
            result['AssetAccountPassword'] = self.asset_account_password
        if self.asset_account_protocol_name is not None:
            result['AssetAccountProtocolName'] = self.asset_account_protocol_name
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetAccountId') is not None:
            self.asset_account_id = m.get('AssetAccountId')
        if m.get('AssetAccountName') is not None:
            self.asset_account_name = m.get('AssetAccountName')
        if m.get('AssetAccountPassword') is not None:
            self.asset_account_password = m.get('AssetAccountPassword')
        if m.get('AssetAccountProtocolName') is not None:
            self.asset_account_protocol_name = m.get('AssetAccountProtocolName')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GenerateAssetOperationTokenResponseBodyAssetOperationToken(TeaModel):
    def __init__(
        self,
        count_left: int = None,
        expire_time: int = None,
        has_count_limit: bool = None,
        max_renew_count: int = None,
        renew_count: int = None,
        token: str = None,
        token_id: str = None,
    ):
        self.count_left = count_left
        self.expire_time = expire_time
        self.has_count_limit = has_count_limit
        self.max_renew_count = max_renew_count
        self.renew_count = renew_count
        self.token = token
        self.token_id = token_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_left is not None:
            result['CountLeft'] = self.count_left
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.has_count_limit is not None:
            result['HasCountLimit'] = self.has_count_limit
        if self.max_renew_count is not None:
            result['MaxRenewCount'] = self.max_renew_count
        if self.renew_count is not None:
            result['RenewCount'] = self.renew_count
        if self.token is not None:
            result['Token'] = self.token
        if self.token_id is not None:
            result['TokenId'] = self.token_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountLeft') is not None:
            self.count_left = m.get('CountLeft')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HasCountLimit') is not None:
            self.has_count_limit = m.get('HasCountLimit')
        if m.get('MaxRenewCount') is not None:
            self.max_renew_count = m.get('MaxRenewCount')
        if m.get('RenewCount') is not None:
            self.renew_count = m.get('RenewCount')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TokenId') is not None:
            self.token_id = m.get('TokenId')
        return self


class GenerateAssetOperationTokenResponseBody(TeaModel):
    def __init__(
        self,
        asset_operation_token: GenerateAssetOperationTokenResponseBodyAssetOperationToken = None,
        request_id: str = None,
    ):
        self.asset_operation_token = asset_operation_token
        self.request_id = request_id

    def validate(self):
        if self.asset_operation_token:
            self.asset_operation_token.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_operation_token is not None:
            result['AssetOperationToken'] = self.asset_operation_token.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetOperationToken') is not None:
            temp_model = GenerateAssetOperationTokenResponseBodyAssetOperationToken()
            self.asset_operation_token = temp_model.from_map(m['AssetOperationToken'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateAssetOperationTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateAssetOperationTokenResponseBody = None,
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
            temp_model = GenerateAssetOperationTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatabaseRequest(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.database_id = database_id
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetDatabaseResponseBodyDatabase(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        database_id: str = None,
        database_name: str = None,
        database_port: int = None,
        database_private_address: str = None,
        database_public_address: str = None,
        database_type: str = None,
        network_domain_id: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_region_id: str = None,
        source_instance_state: str = None,
    ):
        self.active_address_type = active_address_type
        self.comment = comment
        self.database_id = database_id
        self.database_name = database_name
        self.database_port = database_port
        self.database_private_address = database_private_address
        self.database_public_address = database_public_address
        self.database_type = database_type
        self.network_domain_id = network_domain_id
        self.source = source
        self.source_instance_id = source_instance_id
        self.source_instance_region_id = source_instance_region_id
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
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_port is not None:
            result['DatabasePort'] = self.database_port
        if self.database_private_address is not None:
            result['DatabasePrivateAddress'] = self.database_private_address
        if self.database_public_address is not None:
            result['DatabasePublicAddress'] = self.database_public_address
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_instance_region_id is not None:
            result['SourceInstanceRegionId'] = self.source_instance_region_id
        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabasePort') is not None:
            self.database_port = m.get('DatabasePort')
        if m.get('DatabasePrivateAddress') is not None:
            self.database_private_address = m.get('DatabasePrivateAddress')
        if m.get('DatabasePublicAddress') is not None:
            self.database_public_address = m.get('DatabasePublicAddress')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceInstanceRegionId') is not None:
            self.source_instance_region_id = m.get('SourceInstanceRegionId')
        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')
        return self


class GetDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        database: GetDatabaseResponseBodyDatabase = None,
        request_id: str = None,
    ):
        self.database = database
        self.request_id = request_id

    def validate(self):
        if self.database:
            self.database.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            temp_model = GetDatabaseResponseBodyDatabase()
            self.database = temp_model.from_map(m['Database'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatabaseResponseBody = None,
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
            temp_model = GetDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatabaseAccountRequest(TeaModel):
    def __init__(
        self,
        database_account_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.database_account_id = database_account_id
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetDatabaseAccountResponseBodyDatabaseAccount(TeaModel):
    def __init__(
        self,
        database_account_id: str = None,
        database_account_name: str = None,
        database_schema: str = None,
        has_password: bool = None,
        login_attribute: str = None,
    ):
        self.database_account_id = database_account_id
        self.database_account_name = database_account_name
        self.database_schema = database_schema
        self.has_password = has_password
        self.login_attribute = login_attribute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name
        if self.database_schema is not None:
            result['DatabaseSchema'] = self.database_schema
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.login_attribute is not None:
            result['LoginAttribute'] = self.login_attribute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')
        if m.get('DatabaseSchema') is not None:
            self.database_schema = m.get('DatabaseSchema')
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('LoginAttribute') is not None:
            self.login_attribute = m.get('LoginAttribute')
        return self


class GetDatabaseAccountResponseBody(TeaModel):
    def __init__(
        self,
        database_account: GetDatabaseAccountResponseBodyDatabaseAccount = None,
        request_id: str = None,
    ):
        self.database_account = database_account
        self.request_id = request_id

    def validate(self):
        if self.database_account:
            self.database_account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account is not None:
            result['DatabaseAccount'] = self.database_account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccount') is not None:
            temp_model = GetDatabaseAccountResponseBodyDatabaseAccount()
            self.database_account = temp_model.from_map(m['DatabaseAccount'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDatabaseAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatabaseAccountResponseBody = None,
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
            temp_model = GetDatabaseAccountResponseBody()
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
        # The ID of the host group.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_id = host_group_id
        # The ID of the bastion host in which you want to query the details of the host group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host in which you want to query the details of the host group.
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


class GetHostGroupResponseBodyHostGroup(TeaModel):
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


class GetHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        host_group: GetHostGroupResponseBodyHostGroup = None,
        request_id: str = None,
    ):
        # The details of the host group returned.
        self.host_group = host_group
        # The ID of the request.
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
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
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
        # The distinguished name (DN) of the AD server account.
        self.account = account
        # The Base DN of the AD server.
        self.base_dn = base_dn
        # The domain on the AD server.
        self.domain = domain
        # The field that is used to indicate the email address of a user on the AD server.
        self.email_mapping = email_mapping
        # The condition that is used to filter users.
        self.filter = filter
        # Indicates whether passwords are required. Valid values:
        # 
        # *   **true**:
        # *   **false**\
        self.has_password = has_password
        # Indicates whether SSL is supported. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_ssl = is_ssl
        # The field that is used to indicate the mobile phone number of a user on the AD server.
        self.mobile_mapping = mobile_mapping
        # The field that is used to indicate the name of a user on the AD server.
        self.name_mapping = name_mapping
        # The port that is used to access the AD server.
        self.port = port
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
        # The settings of AD authentication.
        self.ad = ad
        # The ID of the request, which is used to locate and troubleshoot issues.
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
        # Indicates whether two-factor authentication is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable_two_factor = enable_two_factor
        # The duration within which two-factor authentication is not required after a local user passes two-factor authentication. Valid values: `0 to 168`. Unit: hours.
        # 
        # > If 0 is returned, a local user must pass two-factor authentication every time the local user logs on to the bastion host.
        self.skip_two_factor_time = skip_two_factor_time
        # The two-factor authentication methods.
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
        # The ID of the request, which is used to locate and troubleshoot issues.
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


class GetNetworkDomainRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        network_domain_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.network_domain_id = network_domain_id
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
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetNetworkDomainResponseBodyNetworkDomainProxies(TeaModel):
    def __init__(
        self,
        address: str = None,
        has_password: bool = None,
        node_type: str = None,
        port: int = None,
        proxy_state: str = None,
        proxy_state_error_code: str = None,
        proxy_type: str = None,
        user: str = None,
    ):
        self.address = address
        self.has_password = has_password
        self.node_type = node_type
        self.port = port
        self.proxy_state = proxy_state
        self.proxy_state_error_code = proxy_state_error_code
        self.proxy_type = proxy_type
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.port is not None:
            result['Port'] = self.port
        if self.proxy_state is not None:
            result['ProxyState'] = self.proxy_state
        if self.proxy_state_error_code is not None:
            result['ProxyStateErrorCode'] = self.proxy_state_error_code
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProxyState') is not None:
            self.proxy_state = m.get('ProxyState')
        if m.get('ProxyStateErrorCode') is not None:
            self.proxy_state_error_code = m.get('ProxyStateErrorCode')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class GetNetworkDomainResponseBodyNetworkDomain(TeaModel):
    def __init__(
        self,
        comment: str = None,
        default: bool = None,
        network_domain_id: str = None,
        network_domain_name: str = None,
        network_domain_type: str = None,
        proxies: List[GetNetworkDomainResponseBodyNetworkDomainProxies] = None,
    ):
        self.comment = comment
        self.default = default
        self.network_domain_id = network_domain_id
        self.network_domain_name = network_domain_name
        self.network_domain_type = network_domain_type
        self.proxies = proxies

    def validate(self):
        if self.proxies:
            for k in self.proxies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.default is not None:
            result['Default'] = self.default
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.network_domain_name is not None:
            result['NetworkDomainName'] = self.network_domain_name
        if self.network_domain_type is not None:
            result['NetworkDomainType'] = self.network_domain_type
        result['Proxies'] = []
        if self.proxies is not None:
            for k in self.proxies:
                result['Proxies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('NetworkDomainName') is not None:
            self.network_domain_name = m.get('NetworkDomainName')
        if m.get('NetworkDomainType') is not None:
            self.network_domain_type = m.get('NetworkDomainType')
        self.proxies = []
        if m.get('Proxies') is not None:
            for k in m.get('Proxies'):
                temp_model = GetNetworkDomainResponseBodyNetworkDomainProxies()
                self.proxies.append(temp_model.from_map(k))
        return self


class GetNetworkDomainResponseBody(TeaModel):
    def __init__(
        self,
        network_domain: GetNetworkDomainResponseBodyNetworkDomain = None,
        request_id: str = None,
    ):
        self.network_domain = network_domain
        self.request_id = request_id

    def validate(self):
        if self.network_domain:
            self.network_domain.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_domain is not None:
            result['NetworkDomain'] = self.network_domain.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkDomain') is not None:
            temp_model = GetNetworkDomainResponseBodyNetworkDomain()
            self.network_domain = temp_model.from_map(m['NetworkDomain'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNetworkDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNetworkDomainResponseBody = None,
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
            temp_model = GetNetworkDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.policy_id = policy_id
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
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPolicyResponseBodyPolicyAccessTimeRangeConfigEffectiveTime(TeaModel):
    def __init__(
        self,
        days: List[str] = None,
        hours: List[str] = None,
    ):
        self.days = days
        self.hours = hours

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days is not None:
            result['Days'] = self.days
        if self.hours is not None:
            result['Hours'] = self.hours
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('Hours') is not None:
            self.hours = m.get('Hours')
        return self


class GetPolicyResponseBodyPolicyAccessTimeRangeConfig(TeaModel):
    def __init__(
        self,
        effective_time: List[GetPolicyResponseBodyPolicyAccessTimeRangeConfigEffectiveTime] = None,
    ):
        self.effective_time = effective_time

    def validate(self):
        if self.effective_time:
            for k in self.effective_time:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EffectiveTime'] = []
        if self.effective_time is not None:
            for k in self.effective_time:
                result['EffectiveTime'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.effective_time = []
        if m.get('EffectiveTime') is not None:
            for k in m.get('EffectiveTime'):
                temp_model = GetPolicyResponseBodyPolicyAccessTimeRangeConfigEffectiveTime()
                self.effective_time.append(temp_model.from_map(k))
        return self


class GetPolicyResponseBodyPolicyApprovalConfig(TeaModel):
    def __init__(
        self,
        switch_status: str = None,
    ):
        self.switch_status = switch_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        return self


class GetPolicyResponseBodyPolicyCommandConfigApproval(TeaModel):
    def __init__(
        self,
        commands: List[str] = None,
    ):
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commands is not None:
            result['Commands'] = self.commands
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        return self


class GetPolicyResponseBodyPolicyCommandConfigDeny(TeaModel):
    def __init__(
        self,
        acl_type: str = None,
        commands: List[str] = None,
    ):
        self.acl_type = acl_type
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.commands is not None:
            result['Commands'] = self.commands
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        return self


class GetPolicyResponseBodyPolicyCommandConfig(TeaModel):
    def __init__(
        self,
        approval: GetPolicyResponseBodyPolicyCommandConfigApproval = None,
        deny: GetPolicyResponseBodyPolicyCommandConfigDeny = None,
    ):
        self.approval = approval
        self.deny = deny

    def validate(self):
        if self.approval:
            self.approval.validate()
        if self.deny:
            self.deny.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval is not None:
            result['Approval'] = self.approval.to_map()
        if self.deny is not None:
            result['Deny'] = self.deny.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Approval') is not None:
            temp_model = GetPolicyResponseBodyPolicyCommandConfigApproval()
            self.approval = temp_model.from_map(m['Approval'])
        if m.get('Deny') is not None:
            temp_model = GetPolicyResponseBodyPolicyCommandConfigDeny()
            self.deny = temp_model.from_map(m['Deny'])
        return self


class GetPolicyResponseBodyPolicyIPAclConfig(TeaModel):
    def __init__(
        self,
        acl_type: str = None,
        ips: List[str] = None,
    ):
        self.acl_type = acl_type
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.ips is not None:
            result['IPs'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('IPs') is not None:
            self.ips = m.get('IPs')
        return self


class GetPolicyResponseBodyPolicyProtocolConfigRDP(TeaModel):
    def __init__(
        self,
        clipboard_download: str = None,
        clipboard_upload: str = None,
        disk_redirection: str = None,
        record_keyboard: str = None,
    ):
        self.clipboard_download = clipboard_download
        self.clipboard_upload = clipboard_upload
        self.disk_redirection = disk_redirection
        self.record_keyboard = record_keyboard

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clipboard_download is not None:
            result['ClipboardDownload'] = self.clipboard_download
        if self.clipboard_upload is not None:
            result['ClipboardUpload'] = self.clipboard_upload
        if self.disk_redirection is not None:
            result['DiskRedirection'] = self.disk_redirection
        if self.record_keyboard is not None:
            result['RecordKeyboard'] = self.record_keyboard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClipboardDownload') is not None:
            self.clipboard_download = m.get('ClipboardDownload')
        if m.get('ClipboardUpload') is not None:
            self.clipboard_upload = m.get('ClipboardUpload')
        if m.get('DiskRedirection') is not None:
            self.disk_redirection = m.get('DiskRedirection')
        if m.get('RecordKeyboard') is not None:
            self.record_keyboard = m.get('RecordKeyboard')
        return self


class GetPolicyResponseBodyPolicyProtocolConfigSSH(TeaModel):
    def __init__(
        self,
        exec_command: str = None,
        sftpchannel: str = None,
        sftpdownload_file: str = None,
        sftpmkdir: str = None,
        sftpremove_file: str = None,
        sftprename_file: str = None,
        sftprmdir: str = None,
        sftpupload_file: str = None,
        sshchannel: str = None,
        x_11forwarding: str = None,
    ):
        self.exec_command = exec_command
        self.sftpchannel = sftpchannel
        self.sftpdownload_file = sftpdownload_file
        self.sftpmkdir = sftpmkdir
        self.sftpremove_file = sftpremove_file
        self.sftprename_file = sftprename_file
        self.sftprmdir = sftprmdir
        self.sftpupload_file = sftpupload_file
        self.sshchannel = sshchannel
        self.x_11forwarding = x_11forwarding

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec_command is not None:
            result['ExecCommand'] = self.exec_command
        if self.sftpchannel is not None:
            result['SFTPChannel'] = self.sftpchannel
        if self.sftpdownload_file is not None:
            result['SFTPDownloadFile'] = self.sftpdownload_file
        if self.sftpmkdir is not None:
            result['SFTPMkdir'] = self.sftpmkdir
        if self.sftpremove_file is not None:
            result['SFTPRemoveFile'] = self.sftpremove_file
        if self.sftprename_file is not None:
            result['SFTPRenameFile'] = self.sftprename_file
        if self.sftprmdir is not None:
            result['SFTPRmdir'] = self.sftprmdir
        if self.sftpupload_file is not None:
            result['SFTPUploadFile'] = self.sftpupload_file
        if self.sshchannel is not None:
            result['SSHChannel'] = self.sshchannel
        if self.x_11forwarding is not None:
            result['X11Forwarding'] = self.x_11forwarding
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecCommand') is not None:
            self.exec_command = m.get('ExecCommand')
        if m.get('SFTPChannel') is not None:
            self.sftpchannel = m.get('SFTPChannel')
        if m.get('SFTPDownloadFile') is not None:
            self.sftpdownload_file = m.get('SFTPDownloadFile')
        if m.get('SFTPMkdir') is not None:
            self.sftpmkdir = m.get('SFTPMkdir')
        if m.get('SFTPRemoveFile') is not None:
            self.sftpremove_file = m.get('SFTPRemoveFile')
        if m.get('SFTPRenameFile') is not None:
            self.sftprename_file = m.get('SFTPRenameFile')
        if m.get('SFTPRmdir') is not None:
            self.sftprmdir = m.get('SFTPRmdir')
        if m.get('SFTPUploadFile') is not None:
            self.sftpupload_file = m.get('SFTPUploadFile')
        if m.get('SSHChannel') is not None:
            self.sshchannel = m.get('SSHChannel')
        if m.get('X11Forwarding') is not None:
            self.x_11forwarding = m.get('X11Forwarding')
        return self


class GetPolicyResponseBodyPolicyProtocolConfig(TeaModel):
    def __init__(
        self,
        rdp: GetPolicyResponseBodyPolicyProtocolConfigRDP = None,
        ssh: GetPolicyResponseBodyPolicyProtocolConfigSSH = None,
    ):
        self.rdp = rdp
        self.ssh = ssh

    def validate(self):
        if self.rdp:
            self.rdp.validate()
        if self.ssh:
            self.ssh.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rdp is not None:
            result['RDP'] = self.rdp.to_map()
        if self.ssh is not None:
            result['SSH'] = self.ssh.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RDP') is not None:
            temp_model = GetPolicyResponseBodyPolicyProtocolConfigRDP()
            self.rdp = temp_model.from_map(m['RDP'])
        if m.get('SSH') is not None:
            temp_model = GetPolicyResponseBodyPolicyProtocolConfigSSH()
            self.ssh = temp_model.from_map(m['SSH'])
        return self


class GetPolicyResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        access_time_range_config: GetPolicyResponseBodyPolicyAccessTimeRangeConfig = None,
        approval_config: GetPolicyResponseBodyPolicyApprovalConfig = None,
        command_config: GetPolicyResponseBodyPolicyCommandConfig = None,
        comment: str = None,
        ipacl_config: GetPolicyResponseBodyPolicyIPAclConfig = None,
        policy_id: str = None,
        policy_name: str = None,
        priority: int = None,
        protocol_config: GetPolicyResponseBodyPolicyProtocolConfig = None,
    ):
        self.access_time_range_config = access_time_range_config
        self.approval_config = approval_config
        self.command_config = command_config
        self.comment = comment
        self.ipacl_config = ipacl_config
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.priority = priority
        self.protocol_config = protocol_config

    def validate(self):
        if self.access_time_range_config:
            self.access_time_range_config.validate()
        if self.approval_config:
            self.approval_config.validate()
        if self.command_config:
            self.command_config.validate()
        if self.ipacl_config:
            self.ipacl_config.validate()
        if self.protocol_config:
            self.protocol_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_time_range_config is not None:
            result['AccessTimeRangeConfig'] = self.access_time_range_config.to_map()
        if self.approval_config is not None:
            result['ApprovalConfig'] = self.approval_config.to_map()
        if self.command_config is not None:
            result['CommandConfig'] = self.command_config.to_map()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.ipacl_config is not None:
            result['IPAclConfig'] = self.ipacl_config.to_map()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.protocol_config is not None:
            result['ProtocolConfig'] = self.protocol_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTimeRangeConfig') is not None:
            temp_model = GetPolicyResponseBodyPolicyAccessTimeRangeConfig()
            self.access_time_range_config = temp_model.from_map(m['AccessTimeRangeConfig'])
        if m.get('ApprovalConfig') is not None:
            temp_model = GetPolicyResponseBodyPolicyApprovalConfig()
            self.approval_config = temp_model.from_map(m['ApprovalConfig'])
        if m.get('CommandConfig') is not None:
            temp_model = GetPolicyResponseBodyPolicyCommandConfig()
            self.command_config = temp_model.from_map(m['CommandConfig'])
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('IPAclConfig') is not None:
            temp_model = GetPolicyResponseBodyPolicyIPAclConfig()
            self.ipacl_config = temp_model.from_map(m['IPAclConfig'])
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ProtocolConfig') is not None:
            temp_model = GetPolicyResponseBodyPolicyProtocolConfig()
            self.protocol_config = temp_model.from_map(m['ProtocolConfig'])
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


class GetPolicyAssetScopeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.policy_id = policy_id
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
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPolicyAssetScopeResponseBodyAssetScopeDatabases(TeaModel):
    def __init__(
        self,
        account_scope_type: str = None,
        database_account_ids: List[str] = None,
        database_id: str = None,
    ):
        self.account_scope_type = account_scope_type
        self.database_account_ids = database_account_ids
        self.database_id = database_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_scope_type is not None:
            result['AccountScopeType'] = self.account_scope_type
        if self.database_account_ids is not None:
            result['DatabaseAccountIds'] = self.database_account_ids
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScopeType') is not None:
            self.account_scope_type = m.get('AccountScopeType')
        if m.get('DatabaseAccountIds') is not None:
            self.database_account_ids = m.get('DatabaseAccountIds')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        return self


class GetPolicyAssetScopeResponseBodyAssetScopeHostGroups(TeaModel):
    def __init__(
        self,
        account_names: List[str] = None,
        account_scope_type: str = None,
        host_group_id: str = None,
    ):
        self.account_names = account_names
        self.account_scope_type = account_scope_type
        self.host_group_id = host_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_names is not None:
            result['AccountNames'] = self.account_names
        if self.account_scope_type is not None:
            result['AccountScopeType'] = self.account_scope_type
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNames') is not None:
            self.account_names = m.get('AccountNames')
        if m.get('AccountScopeType') is not None:
            self.account_scope_type = m.get('AccountScopeType')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class GetPolicyAssetScopeResponseBodyAssetScopeHosts(TeaModel):
    def __init__(
        self,
        account_scope_type: str = None,
        host_account_ids: List[str] = None,
        host_id: str = None,
    ):
        self.account_scope_type = account_scope_type
        self.host_account_ids = host_account_ids
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_scope_type is not None:
            result['AccountScopeType'] = self.account_scope_type
        if self.host_account_ids is not None:
            result['HostAccountIds'] = self.host_account_ids
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScopeType') is not None:
            self.account_scope_type = m.get('AccountScopeType')
        if m.get('HostAccountIds') is not None:
            self.host_account_ids = m.get('HostAccountIds')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class GetPolicyAssetScopeResponseBodyAssetScope(TeaModel):
    def __init__(
        self,
        databases: List[GetPolicyAssetScopeResponseBodyAssetScopeDatabases] = None,
        host_groups: List[GetPolicyAssetScopeResponseBodyAssetScopeHostGroups] = None,
        hosts: List[GetPolicyAssetScopeResponseBodyAssetScopeHosts] = None,
        scope_type: str = None,
    ):
        self.databases = databases
        self.host_groups = host_groups
        self.hosts = hosts
        self.scope_type = scope_type

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = GetPolicyAssetScopeResponseBodyAssetScopeDatabases()
                self.databases.append(temp_model.from_map(k))
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = GetPolicyAssetScopeResponseBodyAssetScopeHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = GetPolicyAssetScopeResponseBodyAssetScopeHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class GetPolicyAssetScopeResponseBody(TeaModel):
    def __init__(
        self,
        asset_scope: GetPolicyAssetScopeResponseBodyAssetScope = None,
        request_id: str = None,
    ):
        self.asset_scope = asset_scope
        self.request_id = request_id

    def validate(self):
        if self.asset_scope:
            self.asset_scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_scope is not None:
            result['AssetScope'] = self.asset_scope.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetScope') is not None:
            temp_model = GetPolicyAssetScopeResponseBodyAssetScope()
            self.asset_scope = temp_model.from_map(m['AssetScope'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPolicyAssetScopeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPolicyAssetScopeResponseBody = None,
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
            temp_model = GetPolicyAssetScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyUserScopeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.policy_id = policy_id
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
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPolicyUserScopeResponseBodyUserScope(TeaModel):
    def __init__(
        self,
        scope_type: str = None,
        user_group_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        self.scope_type = scope_type
        self.user_group_ids = user_group_ids
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class GetPolicyUserScopeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_scope: GetPolicyUserScopeResponseBodyUserScope = None,
    ):
        self.request_id = request_id
        self.user_scope = user_scope

    def validate(self):
        if self.user_scope:
            self.user_scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_scope is not None:
            result['UserScope'] = self.user_scope.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserScope') is not None:
            temp_model = GetPolicyUserScopeResponseBodyUserScope()
            self.user_scope = temp_model.from_map(m['UserScope'])
        return self


class GetPolicyUserScopeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPolicyUserScopeResponseBody = None,
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
            temp_model = GetPolicyUserScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        rule_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.rule_id = rule_id

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
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetRuleResponseBodyRuleDatabasesDatabaseAccounts(TeaModel):
    def __init__(
        self,
        database_account_id: str = None,
    ):
        self.database_account_id = database_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        return self


class GetRuleResponseBodyRuleDatabases(TeaModel):
    def __init__(
        self,
        database_accounts: List[GetRuleResponseBodyRuleDatabasesDatabaseAccounts] = None,
        database_id: str = None,
    ):
        self.database_accounts = database_accounts
        self.database_id = database_id

    def validate(self):
        if self.database_accounts:
            for k in self.database_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatabaseAccounts'] = []
        if self.database_accounts is not None:
            for k in self.database_accounts:
                result['DatabaseAccounts'].append(k.to_map() if k else None)
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_accounts = []
        if m.get('DatabaseAccounts') is not None:
            for k in m.get('DatabaseAccounts'):
                temp_model = GetRuleResponseBodyRuleDatabasesDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k))
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        return self


class GetRuleResponseBodyRuleHostGroups(TeaModel):
    def __init__(
        self,
        host_account_names: List[str] = None,
        host_group_id: str = None,
    ):
        self.host_account_names = host_account_names
        self.host_group_id = host_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_names is not None:
            result['HostAccountNames'] = self.host_account_names
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountNames') is not None:
            self.host_account_names = m.get('HostAccountNames')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class GetRuleResponseBodyRuleHostsHostAccounts(TeaModel):
    def __init__(
        self,
        host_account_id: str = None,
    ):
        self.host_account_id = host_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        return self


class GetRuleResponseBodyRuleHosts(TeaModel):
    def __init__(
        self,
        host_accounts: List[GetRuleResponseBodyRuleHostsHostAccounts] = None,
        host_id: str = None,
    ):
        self.host_accounts = host_accounts
        self.host_id = host_id

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
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = GetRuleResponseBodyRuleHostsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class GetRuleResponseBodyRuleUserGroups(TeaModel):
    def __init__(
        self,
        user_group_id: str = None,
    ):
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class GetRuleResponseBodyRuleUsers(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetRuleResponseBodyRule(TeaModel):
    def __init__(
        self,
        comment: str = None,
        databases: List[GetRuleResponseBodyRuleDatabases] = None,
        effective_end_time: str = None,
        effective_start_time: str = None,
        host_groups: List[GetRuleResponseBodyRuleHostGroups] = None,
        hosts: List[GetRuleResponseBodyRuleHosts] = None,
        rule_id: str = None,
        rule_name: str = None,
        user_groups: List[GetRuleResponseBodyRuleUserGroups] = None,
        users: List[GetRuleResponseBodyRuleUsers] = None,
    ):
        self.comment = comment
        self.databases = databases
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.host_groups = host_groups
        self.hosts = hosts
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.user_groups = user_groups
        self.users = users

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = GetRuleResponseBodyRuleDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = GetRuleResponseBodyRuleHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = GetRuleResponseBodyRuleHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = GetRuleResponseBodyRuleUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = GetRuleResponseBodyRuleUsers()
                self.users.append(temp_model.from_map(k))
        return self


class GetRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rule: GetRuleResponseBodyRule = None,
    ):
        self.request_id = request_id
        self.rule = rule

    def validate(self):
        if self.rule:
            self.rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule is not None:
            result['Rule'] = self.rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rule') is not None:
            temp_model = GetRuleResponseBodyRule()
            self.rule = temp_model.from_map(m['Rule'])
        return self


class GetRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRuleResponseBody = None,
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
            temp_model = GetRuleResponseBody()
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
        # The ID of the bastion host in which you want to query the details of the user group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host in which you want to query the details of the user group.
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
        # The description of the user group.
        self.comment = comment
        # The ID of the group.
        self.user_group_id = user_group_id
        # The name of the user group.
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
        # The request ID.
        self.request_id = request_id
        # The details of the user group returned.
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


class ListDatabaseAccountsRequest(TeaModel):
    def __init__(
        self,
        database_account_name: str = None,
        database_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.database_account_name = database_account_name
        self.database_id = database_id
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
        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
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
        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDatabaseAccountsResponseBodyDatabaseAccounts(TeaModel):
    def __init__(
        self,
        database_account_id: str = None,
        database_account_name: str = None,
        database_id: str = None,
        database_schema: str = None,
        has_password: str = None,
    ):
        self.database_account_id = database_account_id
        self.database_account_name = database_account_name
        self.database_id = database_id
        self.database_schema = database_schema
        self.has_password = has_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_schema is not None:
            result['DatabaseSchema'] = self.database_schema
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseSchema') is not None:
            self.database_schema = m.get('DatabaseSchema')
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        return self


class ListDatabaseAccountsResponseBody(TeaModel):
    def __init__(
        self,
        database_accounts: List[ListDatabaseAccountsResponseBodyDatabaseAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.database_accounts = database_accounts
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.database_accounts:
            for k in self.database_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatabaseAccounts'] = []
        if self.database_accounts is not None:
            for k in self.database_accounts:
                result['DatabaseAccounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_accounts = []
        if m.get('DatabaseAccounts') is not None:
            for k in m.get('DatabaseAccounts'):
                temp_model = ListDatabaseAccountsResponseBodyDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatabaseAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatabaseAccountsResponseBody = None,
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
            temp_model = ListDatabaseAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatabaseAccountsForUserRequest(TeaModel):
    def __init__(
        self,
        database_account_name: str = None,
        database_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        self.database_account_name = database_account_name
        self.database_id = database_id
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
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
        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
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


class ListDatabaseAccountsForUserResponseBodyDatabaseAccounts(TeaModel):
    def __init__(
        self,
        database_account_id: str = None,
        database_account_name: str = None,
        database_id: str = None,
        is_authorized: bool = None,
        protocol_name: str = None,
    ):
        self.database_account_id = database_account_id
        self.database_account_name = database_account_name
        self.database_id = database_id
        self.is_authorized = is_authorized
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class ListDatabaseAccountsForUserResponseBody(TeaModel):
    def __init__(
        self,
        database_accounts: List[ListDatabaseAccountsForUserResponseBodyDatabaseAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.database_accounts = database_accounts
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.database_accounts:
            for k in self.database_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatabaseAccounts'] = []
        if self.database_accounts is not None:
            for k in self.database_accounts:
                result['DatabaseAccounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_accounts = []
        if m.get('DatabaseAccounts') is not None:
            for k in m.get('DatabaseAccounts'):
                temp_model = ListDatabaseAccountsForUserResponseBodyDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatabaseAccountsForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatabaseAccountsForUserResponseBody = None,
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
            temp_model = ListDatabaseAccountsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatabaseAccountsForUserGroupRequest(TeaModel):
    def __init__(
        self,
        database_account_name: str = None,
        database_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        self.database_account_name = database_account_name
        self.database_id = database_id
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
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
        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
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


class ListDatabaseAccountsForUserGroupResponseBodyDatabaseAccounts(TeaModel):
    def __init__(
        self,
        database_account_id: str = None,
        database_account_name: str = None,
        database_id: str = None,
        is_authorized: bool = None,
        protocol_name: str = None,
    ):
        self.database_account_id = database_account_id
        self.database_account_name = database_account_name
        self.database_id = database_id
        self.is_authorized = is_authorized
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class ListDatabaseAccountsForUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        database_accounts: List[ListDatabaseAccountsForUserGroupResponseBodyDatabaseAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.database_accounts = database_accounts
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.database_accounts:
            for k in self.database_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatabaseAccounts'] = []
        if self.database_accounts is not None:
            for k in self.database_accounts:
                result['DatabaseAccounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_accounts = []
        if m.get('DatabaseAccounts') is not None:
            for k in m.get('DatabaseAccounts'):
                temp_model = ListDatabaseAccountsForUserGroupResponseBodyDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatabaseAccountsForUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatabaseAccountsForUserGroupResponseBody = None,
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
            temp_model = ListDatabaseAccountsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatabasesRequest(TeaModel):
    def __init__(
        self,
        database_type: str = None,
        host_group_id: str = None,
        instance_id: str = None,
        network_domain_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        source: str = None,
    ):
        self.database_type = database_type
        self.host_group_id = host_group_id
        self.instance_id = instance_id
        self.network_domain_id = network_domain_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListDatabasesResponseBodyDatabases(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        database_id: str = None,
        database_name: str = None,
        database_port: int = None,
        database_private_address: str = None,
        database_public_address: str = None,
        database_type: str = None,
        network_domain_id: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_region_id: str = None,
        source_instance_state: str = None,
    ):
        self.active_address_type = active_address_type
        self.comment = comment
        self.database_id = database_id
        self.database_name = database_name
        self.database_port = database_port
        self.database_private_address = database_private_address
        self.database_public_address = database_public_address
        self.database_type = database_type
        self.network_domain_id = network_domain_id
        self.source = source
        self.source_instance_id = source_instance_id
        self.source_instance_region_id = source_instance_region_id
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
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_port is not None:
            result['DatabasePort'] = self.database_port
        if self.database_private_address is not None:
            result['DatabasePrivateAddress'] = self.database_private_address
        if self.database_public_address is not None:
            result['DatabasePublicAddress'] = self.database_public_address
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_instance_region_id is not None:
            result['SourceInstanceRegionId'] = self.source_instance_region_id
        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabasePort') is not None:
            self.database_port = m.get('DatabasePort')
        if m.get('DatabasePrivateAddress') is not None:
            self.database_private_address = m.get('DatabasePrivateAddress')
        if m.get('DatabasePublicAddress') is not None:
            self.database_public_address = m.get('DatabasePublicAddress')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceInstanceRegionId') is not None:
            self.source_instance_region_id = m.get('SourceInstanceRegionId')
        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')
        return self


class ListDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        databases: List[ListDatabasesResponseBodyDatabases] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.databases = databases
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = ListDatabasesResponseBodyDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatabasesResponseBody = None,
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
            temp_model = ListDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatabasesForUserRequest(TeaModel):
    def __init__(
        self,
        database_address: str = None,
        database_name: str = None,
        database_type: str = None,
        instance_id: str = None,
        network_domain_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        self.database_address = database_address
        self.database_name = database_name
        self.database_type = database_type
        self.instance_id = instance_id
        self.network_domain_id = network_domain_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_address is not None:
            result['DatabaseAddress'] = self.database_address
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
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
        if m.get('DatabaseAddress') is not None:
            self.database_address = m.get('DatabaseAddress')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListDatabasesForUserResponseBodyDatabases(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        database_id: str = None,
        database_name: str = None,
        database_port: int = None,
        database_private_address: str = None,
        database_public_address: str = None,
        database_type: str = None,
        network_domain_id: str = None,
        source: str = None,
        source_instance_id: str = None,
    ):
        self.active_address_type = active_address_type
        self.comment = comment
        self.database_id = database_id
        self.database_name = database_name
        self.database_port = database_port
        self.database_private_address = database_private_address
        self.database_public_address = database_public_address
        self.database_type = database_type
        self.network_domain_id = network_domain_id
        self.source = source
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
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_port is not None:
            result['DatabasePort'] = self.database_port
        if self.database_private_address is not None:
            result['DatabasePrivateAddress'] = self.database_private_address
        if self.database_public_address is not None:
            result['DatabasePublicAddress'] = self.database_public_address
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
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
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabasePort') is not None:
            self.database_port = m.get('DatabasePort')
        if m.get('DatabasePrivateAddress') is not None:
            self.database_private_address = m.get('DatabasePrivateAddress')
        if m.get('DatabasePublicAddress') is not None:
            self.database_public_address = m.get('DatabasePublicAddress')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        return self


class ListDatabasesForUserResponseBody(TeaModel):
    def __init__(
        self,
        databases: List[ListDatabasesForUserResponseBodyDatabases] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.databases = databases
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = ListDatabasesForUserResponseBodyDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatabasesForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatabasesForUserResponseBody = None,
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
            temp_model = ListDatabasesForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatabasesForUserGroupRequest(TeaModel):
    def __init__(
        self,
        database_address: str = None,
        database_name: str = None,
        database_type: str = None,
        instance_id: str = None,
        network_domain_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        self.database_address = database_address
        self.database_name = database_name
        self.database_type = database_type
        self.instance_id = instance_id
        self.network_domain_id = network_domain_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_address is not None:
            result['DatabaseAddress'] = self.database_address
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
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
        if m.get('DatabaseAddress') is not None:
            self.database_address = m.get('DatabaseAddress')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListDatabasesForUserGroupResponseBodyDatabases(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        database_account_count: int = None,
        database_id: str = None,
        database_name: str = None,
        database_port: int = None,
        database_private_address: str = None,
        database_public_address: str = None,
        database_type: str = None,
        network_domain_id: str = None,
        source: str = None,
        source_instance_id: str = None,
    ):
        self.active_address_type = active_address_type
        self.comment = comment
        self.database_account_count = database_account_count
        self.database_id = database_id
        self.database_name = database_name
        self.database_port = database_port
        self.database_private_address = database_private_address
        self.database_public_address = database_public_address
        self.database_type = database_type
        self.network_domain_id = network_domain_id
        self.source = source
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
        if self.database_account_count is not None:
            result['DatabaseAccountCount'] = self.database_account_count
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_port is not None:
            result['DatabasePort'] = self.database_port
        if self.database_private_address is not None:
            result['DatabasePrivateAddress'] = self.database_private_address
        if self.database_public_address is not None:
            result['DatabasePublicAddress'] = self.database_public_address
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
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
        if m.get('DatabaseAccountCount') is not None:
            self.database_account_count = m.get('DatabaseAccountCount')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabasePort') is not None:
            self.database_port = m.get('DatabasePort')
        if m.get('DatabasePrivateAddress') is not None:
            self.database_private_address = m.get('DatabasePrivateAddress')
        if m.get('DatabasePublicAddress') is not None:
            self.database_public_address = m.get('DatabasePublicAddress')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        return self


class ListDatabasesForUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        databases: List[ListDatabasesForUserGroupResponseBodyDatabases] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.databases = databases
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = ListDatabasesForUserGroupResponseBodyDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatabasesForUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatabasesForUserGroupResponseBody = None,
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
            temp_model = ListDatabasesForUserGroupResponseBody()
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
        # The name of the host account that you want to query. The name can be up to 128 characters in length. Only exact match is supported.
        self.host_account_name = host_account_name
        # The ID of the specified host whose accounts you want to query.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.host_id = host_id
        # The ID of the bastion host in which you want to query accounts of the specified host.
        # 
        # >  You can call the DescribeInstances operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The protocol used by the host whose accounts you want to query.
        # 
        # Valid values:
        # 
        # *   SSH
        # *   RDP
        self.protocol_name = protocol_name
        # The region ID of the bastion host in which you want to query accounts of the specified host.
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
        # Indicates whether a password is configured for the host account.
        # 
        # Valid values:
        # 
        # *   true: A password is configured for the host account.
        # *   false: No passwords are configured for the host account.
        self.has_password = has_password
        # The ID of the host account.
        self.host_account_id = host_account_id
        # The name of the host account.
        self.host_account_name = host_account_name
        # The ID of the host.
        self.host_id = host_id
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The name of the shared key.
        self.host_share_key_name = host_share_key_name
        # The fingerprint of the private key for the host account.
        self.private_key_fingerprint = private_key_fingerprint
        # The protocol that is used by the host.
        # 
        # Valid values:
        # 
        # *   SSH
        # *   RDP
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
        # An array that consists of the queried host accounts.
        self.host_accounts = host_accounts
        # The ID of the request.
        self.request_id = request_id
        # The total number of host accounts that are queried.
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
        # The name of the host account that you want to query. Exact match is supported.
        self.host_account_name = host_account_name
        # The ID of the host to query.
        # 
        # > You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.host_id = host_id
        # The ID of the bastion host on which you want to perform the query. The host accounts that the specified user is authorized to manage on the specified host are queried.
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
        # The region ID of the bastion host on which you want to perform the query. The host accounts that the specified user is authorized to manage on the specified host are queried.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id
        # The ID of the user for which you want to query authorized host accounts.
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
        # The ID of the host account.
        self.host_account_id = host_account_id
        # The name of the host account.
        self.host_account_name = host_account_name
        # The ID of the host for which the host accounts were queried.
        self.host_id = host_id
        # Indicates whether the user is authorized to manage the host account. Valid values:
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


class ListHostAccountsForUserResponseBody(TeaModel):
    def __init__(
        self,
        host_accounts: List[ListHostAccountsForUserResponseBodyHostAccounts] = None,
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


class ListNetworkDomainsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        network_domain_name: str = None,
        network_domain_type: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.network_domain_name = network_domain_name
        self.network_domain_type = network_domain_type
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
        if self.network_domain_name is not None:
            result['NetworkDomainName'] = self.network_domain_name
        if self.network_domain_type is not None:
            result['NetworkDomainType'] = self.network_domain_type
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
        if m.get('NetworkDomainName') is not None:
            self.network_domain_name = m.get('NetworkDomainName')
        if m.get('NetworkDomainType') is not None:
            self.network_domain_type = m.get('NetworkDomainType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListNetworkDomainsResponseBodyNetworkDomainsProxiesState(TeaModel):
    def __init__(
        self,
        node_type: str = None,
        proxy_state: str = None,
    ):
        self.node_type = node_type
        self.proxy_state = proxy_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.proxy_state is not None:
            result['ProxyState'] = self.proxy_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('ProxyState') is not None:
            self.proxy_state = m.get('ProxyState')
        return self


class ListNetworkDomainsResponseBodyNetworkDomains(TeaModel):
    def __init__(
        self,
        comment: str = None,
        default: bool = None,
        network_domain_id: str = None,
        network_domain_name: str = None,
        network_domain_type: str = None,
        proxies_state: List[ListNetworkDomainsResponseBodyNetworkDomainsProxiesState] = None,
    ):
        self.comment = comment
        self.default = default
        self.network_domain_id = network_domain_id
        self.network_domain_name = network_domain_name
        self.network_domain_type = network_domain_type
        self.proxies_state = proxies_state

    def validate(self):
        if self.proxies_state:
            for k in self.proxies_state:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.default is not None:
            result['Default'] = self.default
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.network_domain_name is not None:
            result['NetworkDomainName'] = self.network_domain_name
        if self.network_domain_type is not None:
            result['NetworkDomainType'] = self.network_domain_type
        result['ProxiesState'] = []
        if self.proxies_state is not None:
            for k in self.proxies_state:
                result['ProxiesState'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('NetworkDomainName') is not None:
            self.network_domain_name = m.get('NetworkDomainName')
        if m.get('NetworkDomainType') is not None:
            self.network_domain_type = m.get('NetworkDomainType')
        self.proxies_state = []
        if m.get('ProxiesState') is not None:
            for k in m.get('ProxiesState'):
                temp_model = ListNetworkDomainsResponseBodyNetworkDomainsProxiesState()
                self.proxies_state.append(temp_model.from_map(k))
        return self


class ListNetworkDomainsResponseBody(TeaModel):
    def __init__(
        self,
        network_domains: List[ListNetworkDomainsResponseBodyNetworkDomains] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.network_domains = network_domains
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.network_domains:
            for k in self.network_domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NetworkDomains'] = []
        if self.network_domains is not None:
            for k in self.network_domains:
                result['NetworkDomains'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_domains = []
        if m.get('NetworkDomains') is not None:
            for k in m.get('NetworkDomains'):
                temp_model = ListNetworkDomainsResponseBodyNetworkDomains()
                self.network_domains.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNetworkDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNetworkDomainsResponseBody = None,
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
            temp_model = ListNetworkDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOperationDatabaseAccountsRequest(TeaModel):
    def __init__(
        self,
        database_account_name: str = None,
        database_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.database_account_name = database_account_name
        self.database_id = database_id
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
        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
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
        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListOperationDatabaseAccountsResponseBodyDatabaseAccounts(TeaModel):
    def __init__(
        self,
        dbname: str = None,
        database_account_id: str = None,
        database_account_name: str = None,
        database_id: str = None,
        has_password: str = None,
        login_attribute: str = None,
        protocol_name: str = None,
    ):
        self.dbname = dbname
        self.database_account_id = database_account_id
        self.database_account_name = database_account_name
        self.database_id = database_id
        self.has_password = has_password
        self.login_attribute = login_attribute
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.login_attribute is not None:
            result['LoginAttribute'] = self.login_attribute
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('LoginAttribute') is not None:
            self.login_attribute = m.get('LoginAttribute')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class ListOperationDatabaseAccountsResponseBody(TeaModel):
    def __init__(
        self,
        database_accounts: List[ListOperationDatabaseAccountsResponseBodyDatabaseAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.database_accounts = database_accounts
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.database_accounts:
            for k in self.database_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatabaseAccounts'] = []
        if self.database_accounts is not None:
            for k in self.database_accounts:
                result['DatabaseAccounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_accounts = []
        if m.get('DatabaseAccounts') is not None:
            for k in m.get('DatabaseAccounts'):
                temp_model = ListOperationDatabaseAccountsResponseBodyDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOperationDatabaseAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOperationDatabaseAccountsResponseBody = None,
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
            temp_model = ListOperationDatabaseAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOperationDatabasesRequest(TeaModel):
    def __init__(
        self,
        database_address: str = None,
        database_name: str = None,
        database_type: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_state: str = None,
    ):
        self.database_address = database_address
        self.database_name = database_name
        self.database_type = database_type
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.source = source
        self.source_instance_id = source_instance_id
        self.source_instance_state = source_instance_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_address is not None:
            result['DatabaseAddress'] = self.database_address
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('DatabaseAddress') is not None:
            self.database_address = m.get('DatabaseAddress')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class ListOperationDatabasesResponseBodyDatabases(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        database_id: str = None,
        database_name: str = None,
        database_port: int = None,
        database_private_address: str = None,
        database_public_address: str = None,
        database_type: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_region_id: str = None,
        source_instance_state: str = None,
    ):
        self.active_address_type = active_address_type
        self.comment = comment
        self.database_id = database_id
        self.database_name = database_name
        self.database_port = database_port
        self.database_private_address = database_private_address
        self.database_public_address = database_public_address
        self.database_type = database_type
        self.source = source
        self.source_instance_id = source_instance_id
        self.source_instance_region_id = source_instance_region_id
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
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_port is not None:
            result['DatabasePort'] = self.database_port
        if self.database_private_address is not None:
            result['DatabasePrivateAddress'] = self.database_private_address
        if self.database_public_address is not None:
            result['DatabasePublicAddress'] = self.database_public_address
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_instance_region_id is not None:
            result['SourceInstanceRegionId'] = self.source_instance_region_id
        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabasePort') is not None:
            self.database_port = m.get('DatabasePort')
        if m.get('DatabasePrivateAddress') is not None:
            self.database_private_address = m.get('DatabasePrivateAddress')
        if m.get('DatabasePublicAddress') is not None:
            self.database_public_address = m.get('DatabasePublicAddress')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceInstanceRegionId') is not None:
            self.source_instance_region_id = m.get('SourceInstanceRegionId')
        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')
        return self


class ListOperationDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        databases: List[ListOperationDatabasesResponseBodyDatabases] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.databases = databases
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = ListOperationDatabasesResponseBodyDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOperationDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOperationDatabasesResponseBody = None,
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
            temp_model = ListOperationDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOperationHostAccountsRequest(TeaModel):
    def __init__(
        self,
        host_account_name: str = None,
        host_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.host_account_name = host_account_name
        self.host_id = host_id
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
        return self


class ListOperationHostAccountsResponseBodyHostAccountsSSHConfig(TeaModel):
    def __init__(
        self,
        enable_sftpchannel: bool = None,
        enable_sshchannel: bool = None,
    ):
        self.enable_sftpchannel = enable_sftpchannel
        self.enable_sshchannel = enable_sshchannel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_sftpchannel is not None:
            result['EnableSFTPChannel'] = self.enable_sftpchannel
        if self.enable_sshchannel is not None:
            result['EnableSSHChannel'] = self.enable_sshchannel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSFTPChannel') is not None:
            self.enable_sftpchannel = m.get('EnableSFTPChannel')
        if m.get('EnableSSHChannel') is not None:
            self.enable_sshchannel = m.get('EnableSSHChannel')
        return self


class ListOperationHostAccountsResponseBodyHostAccounts(TeaModel):
    def __init__(
        self,
        has_password: bool = None,
        host_account_id: str = None,
        host_account_name: str = None,
        host_id: str = None,
        host_share_key_id: str = None,
        private_key_fingerprint: str = None,
        protocol_name: str = None,
        sshconfig: ListOperationHostAccountsResponseBodyHostAccountsSSHConfig = None,
    ):
        self.has_password = has_password
        self.host_account_id = host_account_id
        self.host_account_name = host_account_name
        self.host_id = host_id
        self.host_share_key_id = host_share_key_id
        self.private_key_fingerprint = private_key_fingerprint
        self.protocol_name = protocol_name
        self.sshconfig = sshconfig

    def validate(self):
        if self.sshconfig:
            self.sshconfig.validate()

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
        if self.private_key_fingerprint is not None:
            result['PrivateKeyFingerprint'] = self.private_key_fingerprint
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.sshconfig is not None:
            result['SSHConfig'] = self.sshconfig.to_map()
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
        if m.get('PrivateKeyFingerprint') is not None:
            self.private_key_fingerprint = m.get('PrivateKeyFingerprint')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('SSHConfig') is not None:
            temp_model = ListOperationHostAccountsResponseBodyHostAccountsSSHConfig()
            self.sshconfig = temp_model.from_map(m['SSHConfig'])
        return self


class ListOperationHostAccountsResponseBody(TeaModel):
    def __init__(
        self,
        host_accounts: List[ListOperationHostAccountsResponseBodyHostAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.host_accounts = host_accounts
        self.request_id = request_id
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
                temp_model = ListOperationHostAccountsResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOperationHostAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOperationHostAccountsResponseBody = None,
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
            temp_model = ListOperationHostAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOperationHostsRequest(TeaModel):
    def __init__(
        self,
        host_address: str = None,
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
        self.host_address = host_address
        self.host_name = host_name
        self.instance_id = instance_id
        self.ostype = ostype
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.source = source
        self.source_instance_id = source_instance_id
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


class ListOperationHostsResponseBodyHosts(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        host_id: str = None,
        host_name: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        ostype: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_state: str = None,
    ):
        self.active_address_type = active_address_type
        self.comment = comment
        self.host_id = host_id
        self.host_name = host_name
        self.host_private_address = host_private_address
        self.host_public_address = host_public_address
        self.ostype = ostype
        self.source = source
        self.source_instance_id = source_instance_id
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


class ListOperationHostsResponseBody(TeaModel):
    def __init__(
        self,
        hosts: List[ListOperationHostsResponseBodyHosts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.hosts = hosts
        self.request_id = request_id
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
                temp_model = ListOperationHostsResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOperationHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOperationHostsResponseBody = None,
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
            temp_model = ListOperationHostsResponseBody()
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


class ListPoliciesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        policy_name: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.policy_name = policy_name
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
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
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
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListPoliciesResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        comment: str = None,
        policy_id: str = None,
        policy_name: str = None,
        priority: int = None,
    ):
        self.comment = comment
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.priority is not None:
            result['Priority'] = self.priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        return self


class ListPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        policies: List[ListPoliciesResponseBodyPolicies] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.policies = policies
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
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


class ListRulesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        rule_name: str = None,
        rule_state: str = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.rule_name = rule_name
        self.rule_state = rule_state

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
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_state is not None:
            result['RuleState'] = self.rule_state
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
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleState') is not None:
            self.rule_state = m.get('RuleState')
        return self


class ListRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        comment: str = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_state: str = None,
    ):
        self.comment = comment
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_state = rule_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_state is not None:
            result['RuleState'] = self.rule_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleState') is not None:
            self.rule_state = m.get('RuleState')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rules: List[ListRulesResponseBodyRules] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.rules = rules
        self.total_count = total_count

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRulesResponseBody = None,
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
            temp_model = ListRulesResponseBody()
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
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20.
        self.key = key
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20.
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
        # The token for starting the next query.
        self.next_token = next_token
        # The region ID of the Bastionhost instance.
        self.region_id = region_id
        # The IDs of instances. The ID is up to 20.
        self.resource_id = resource_id
        # The type of the resource.
        # 
        # Set the value to INSTANCE, which indicates that the resource is a Bastionhost instance.
        self.resource_type = resource_type
        # The tags.
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
        # The ID of the instance.
        self.resource_id = resource_id
        # The type of the resource.
        # 
        # The returned value is INSTANCE, which indicates that the resource is a Bastionhost instance.
        self.resource_type = resource_type
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
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
        # The token for starting the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information about Bastionhost instances and the tags bound to Bastionhost instances.
        # 
        # The following information is included: instance ID, resource type, tag key, and tag value.
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


class ModifyDatabaseRequest(TeaModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        database_id: str = None,
        database_name: str = None,
        database_port: str = None,
        database_private_address: str = None,
        database_public_address: str = None,
        instance_id: str = None,
        network_domain_id: str = None,
        region_id: str = None,
        source_instance_id: str = None,
    ):
        self.active_address_type = active_address_type
        self.comment = comment
        self.database_id = database_id
        self.database_name = database_name
        self.database_port = database_port
        self.database_private_address = database_private_address
        self.database_public_address = database_public_address
        self.instance_id = instance_id
        self.network_domain_id = network_domain_id
        self.region_id = region_id
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
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_port is not None:
            result['DatabasePort'] = self.database_port
        if self.database_private_address is not None:
            result['DatabasePrivateAddress'] = self.database_private_address
        if self.database_public_address is not None:
            result['DatabasePublicAddress'] = self.database_public_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabasePort') is not None:
            self.database_port = m.get('DatabasePort')
        if m.get('DatabasePrivateAddress') is not None:
            self.database_private_address = m.get('DatabasePrivateAddress')
        if m.get('DatabasePublicAddress') is not None:
            self.database_public_address = m.get('DatabasePublicAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        return self


class ModifyDatabaseResponseBody(TeaModel):
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


class ModifyDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDatabaseResponseBody = None,
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
            temp_model = ModifyDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDatabaseAccountRequest(TeaModel):
    def __init__(
        self,
        database_account_id: str = None,
        database_account_name: str = None,
        database_schema: str = None,
        instance_id: str = None,
        password: str = None,
        region_id: str = None,
    ):
        self.database_account_id = database_account_id
        self.database_account_name = database_account_name
        self.database_schema = database_schema
        self.instance_id = instance_id
        self.password = password
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id
        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name
        if self.database_schema is not None:
            result['DatabaseSchema'] = self.database_schema
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')
        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')
        if m.get('DatabaseSchema') is not None:
            self.database_schema = m.get('DatabaseSchema')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDatabaseAccountResponseBody(TeaModel):
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


class ModifyDatabaseAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDatabaseAccountResponseBody = None,
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
            temp_model = ModifyDatabaseAccountResponseBody()
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
        # The new description of the host group. The value can be up to 500 characters in length.
        self.comment = comment
        # The ID of the host group that you want to modify.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_id = host_group_id
        # The new name of the host group. The name can be up to 128 characters in length.
        self.host_group_name = host_group_name
        # The ID of the bastion host on which you want to modify the information about the host group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The region ID of the bastion host on which you want to modify the information about the host group.
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


class ModifyNetworkDomainRequestProxies(TeaModel):
    def __init__(
        self,
        address: str = None,
        node_type: str = None,
        password: str = None,
        port: int = None,
        proxy_type: str = None,
        user: str = None,
    ):
        self.address = address
        self.node_type = node_type
        self.password = password
        self.port = port
        self.proxy_type = proxy_type
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class ModifyNetworkDomainRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        network_domain_id: str = None,
        network_domain_name: str = None,
        network_domain_type: str = None,
        proxies: List[ModifyNetworkDomainRequestProxies] = None,
        region_id: str = None,
    ):
        self.comment = comment
        self.instance_id = instance_id
        self.network_domain_id = network_domain_id
        self.network_domain_name = network_domain_name
        self.network_domain_type = network_domain_type
        self.proxies = proxies
        self.region_id = region_id

    def validate(self):
        if self.proxies:
            for k in self.proxies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.network_domain_name is not None:
            result['NetworkDomainName'] = self.network_domain_name
        if self.network_domain_type is not None:
            result['NetworkDomainType'] = self.network_domain_type
        result['Proxies'] = []
        if self.proxies is not None:
            for k in self.proxies:
                result['Proxies'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('NetworkDomainName') is not None:
            self.network_domain_name = m.get('NetworkDomainName')
        if m.get('NetworkDomainType') is not None:
            self.network_domain_type = m.get('NetworkDomainType')
        self.proxies = []
        if m.get('Proxies') is not None:
            for k in m.get('Proxies'):
                temp_model = ModifyNetworkDomainRequestProxies()
                self.proxies.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyNetworkDomainResponseBody(TeaModel):
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


class ModifyNetworkDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNetworkDomainResponseBody = None,
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
            temp_model = ModifyNetworkDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        policy_id: str = None,
        policy_name: str = None,
        priority: str = None,
        region_id: str = None,
    ):
        self.comment = comment
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.priority = priority
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyPolicyResponseBody(TeaModel):
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


class ModifyPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPolicyResponseBody = None,
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
            temp_model = ModifyPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRuleRequestDatabases(TeaModel):
    def __init__(
        self,
        database_account_ids: List[str] = None,
        database_id: str = None,
    ):
        self.database_account_ids = database_account_ids
        self.database_id = database_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_account_ids is not None:
            result['DatabaseAccountIds'] = self.database_account_ids
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountIds') is not None:
            self.database_account_ids = m.get('DatabaseAccountIds')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        return self


class ModifyRuleRequestHostGroups(TeaModel):
    def __init__(
        self,
        host_account_names: List[str] = None,
        host_group_id: str = None,
    ):
        self.host_account_names = host_account_names
        self.host_group_id = host_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_names is not None:
            result['HostAccountNames'] = self.host_account_names
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountNames') is not None:
            self.host_account_names = m.get('HostAccountNames')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class ModifyRuleRequestHosts(TeaModel):
    def __init__(
        self,
        host_account_ids: List[str] = None,
        host_id: str = None,
    ):
        self.host_account_ids = host_account_ids
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_ids is not None:
            result['HostAccountIds'] = self.host_account_ids
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountIds') is not None:
            self.host_account_ids = m.get('HostAccountIds')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class ModifyRuleRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        databases: List[ModifyRuleRequestDatabases] = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        host_groups: List[ModifyRuleRequestHostGroups] = None,
        hosts: List[ModifyRuleRequestHosts] = None,
        instance_id: str = None,
        region_id: str = None,
        rule_id: str = None,
        rule_name: str = None,
        user_group_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        self.comment = comment
        self.databases = databases
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.host_groups = host_groups
        self.hosts = hosts
        self.instance_id = instance_id
        self.region_id = region_id
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.user_group_ids = user_group_ids
        self.user_ids = user_ids

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = ModifyRuleRequestDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = ModifyRuleRequestHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = ModifyRuleRequestHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class ModifyRuleResponseBody(TeaModel):
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


class ModifyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyRuleResponseBody = None,
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
            temp_model = ModifyRuleResponseBody()
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


class ModifyUserPublicKeyRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        public_key: str = None,
        public_key_id: str = None,
        public_key_name: str = None,
        region_id: str = None,
    ):
        # The new description of the user group. The description can be up to 500 characters in length.
        self.comment = comment
        # The ID of the bastion host that is used to modify the public key of the user.
        # 
        # > You can call the [describeinstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id
        # The new public key.
        # 
        # > The public key must be encoded in Base64.
        self.public_key = public_key
        # The ID of the public key that you want to modify.
        self.public_key_id = public_key_id
        # The name of the public key that you want to modify. This name can be up to 128 characters in length.
        self.public_key_name = public_key_name
        # The region ID of the bastion host that is used to modify the public key of the user.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id
        if self.public_key_name is not None:
            result['PublicKeyName'] = self.public_key_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')
        if m.get('PublicKeyName') is not None:
            self.public_key_name = m.get('PublicKeyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyUserPublicKeyResponseBody(TeaModel):
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


class ModifyUserPublicKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyUserPublicKeyResponseBody = None,
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
            temp_model = ModifyUserPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveDatabasesToNetworkDomainRequest(TeaModel):
    def __init__(
        self,
        database_ids: List[str] = None,
        instance_id: str = None,
        network_domain_id: str = None,
        region_id: str = None,
    ):
        self.database_ids = database_ids
        self.instance_id = instance_id
        self.network_domain_id = network_domain_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_ids is not None:
            result['DatabaseIds'] = self.database_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseIds') is not None:
            self.database_ids = m.get('DatabaseIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class MoveDatabasesToNetworkDomainResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.database_id = database_id
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
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class MoveDatabasesToNetworkDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[MoveDatabasesToNetworkDomainResponseBodyResults] = None,
    ):
        self.request_id = request_id
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
                temp_model = MoveDatabasesToNetworkDomainResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class MoveDatabasesToNetworkDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveDatabasesToNetworkDomainResponseBody = None,
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
            temp_model = MoveDatabasesToNetworkDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveHostsToNetworkDomainRequest(TeaModel):
    def __init__(
        self,
        host_ids: List[str] = None,
        instance_id: str = None,
        network_domain_id: str = None,
        region_id: str = None,
    ):
        self.host_ids = host_ids
        self.instance_id = instance_id
        self.network_domain_id = network_domain_id
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
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class MoveHostsToNetworkDomainResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.host_id = host_id
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


class MoveHostsToNetworkDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[MoveHostsToNetworkDomainResponseBodyResults] = None,
    ):
        self.request_id = request_id
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
                temp_model = MoveHostsToNetworkDomainResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class MoveHostsToNetworkDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveHostsToNetworkDomainResponseBody = None,
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
            temp_model = MoveHostsToNetworkDomainResponseBody()
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


class RemoveDatabasesFromGroupRequest(TeaModel):
    def __init__(
        self,
        database_ids: List[str] = None,
        host_group_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.database_ids = database_ids
        self.host_group_id = host_group_id
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_ids is not None:
            result['DatabaseIds'] = self.database_ids
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseIds') is not None:
            self.database_ids = m.get('DatabaseIds')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RemoveDatabasesFromGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_id: str = None,
        host_group_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.database_id = database_id
        self.host_group_id = host_group_id
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
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveDatabasesFromGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[RemoveDatabasesFromGroupResponseBodyResults] = None,
    ):
        self.request_id = request_id
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
                temp_model = RemoveDatabasesFromGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class RemoveDatabasesFromGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveDatabasesFromGroupResponseBody = None,
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
            temp_model = RemoveDatabasesFromGroupResponseBody()
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


class RenewAssetOperationTokenRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        token_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.token_id = token_id

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
        if self.token_id is not None:
            result['TokenId'] = self.token_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TokenId') is not None:
            self.token_id = m.get('TokenId')
        return self


class RenewAssetOperationTokenResponseBody(TeaModel):
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


class RenewAssetOperationTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewAssetOperationTokenResponseBody = None,
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
            temp_model = RenewAssetOperationTokenResponseBody()
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


class SetPolicyAccessTimeRangeConfigRequestAccessTimeRangeConfigEffectiveTime(TeaModel):
    def __init__(
        self,
        days: List[int] = None,
        hours: List[int] = None,
    ):
        self.days = days
        self.hours = hours

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days is not None:
            result['Days'] = self.days
        if self.hours is not None:
            result['Hours'] = self.hours
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('Hours') is not None:
            self.hours = m.get('Hours')
        return self


class SetPolicyAccessTimeRangeConfigRequestAccessTimeRangeConfig(TeaModel):
    def __init__(
        self,
        effective_time: List[SetPolicyAccessTimeRangeConfigRequestAccessTimeRangeConfigEffectiveTime] = None,
    ):
        self.effective_time = effective_time

    def validate(self):
        if self.effective_time:
            for k in self.effective_time:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EffectiveTime'] = []
        if self.effective_time is not None:
            for k in self.effective_time:
                result['EffectiveTime'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.effective_time = []
        if m.get('EffectiveTime') is not None:
            for k in m.get('EffectiveTime'):
                temp_model = SetPolicyAccessTimeRangeConfigRequestAccessTimeRangeConfigEffectiveTime()
                self.effective_time.append(temp_model.from_map(k))
        return self


class SetPolicyAccessTimeRangeConfigRequest(TeaModel):
    def __init__(
        self,
        access_time_range_config: SetPolicyAccessTimeRangeConfigRequestAccessTimeRangeConfig = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.access_time_range_config = access_time_range_config
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.region_id = region_id

    def validate(self):
        if self.access_time_range_config:
            self.access_time_range_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_time_range_config is not None:
            result['AccessTimeRangeConfig'] = self.access_time_range_config.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTimeRangeConfig') is not None:
            temp_model = SetPolicyAccessTimeRangeConfigRequestAccessTimeRangeConfig()
            self.access_time_range_config = temp_model.from_map(m['AccessTimeRangeConfig'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetPolicyAccessTimeRangeConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        access_time_range_config_shrink: str = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.access_time_range_config_shrink = access_time_range_config_shrink
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_time_range_config_shrink is not None:
            result['AccessTimeRangeConfig'] = self.access_time_range_config_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTimeRangeConfig') is not None:
            self.access_time_range_config_shrink = m.get('AccessTimeRangeConfig')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetPolicyAccessTimeRangeConfigResponseBody(TeaModel):
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


class SetPolicyAccessTimeRangeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetPolicyAccessTimeRangeConfigResponseBody = None,
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
            temp_model = SetPolicyAccessTimeRangeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPolicyApprovalConfigRequestApprovalConfig(TeaModel):
    def __init__(
        self,
        switch_status: str = None,
    ):
        self.switch_status = switch_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        return self


class SetPolicyApprovalConfigRequest(TeaModel):
    def __init__(
        self,
        approval_config: SetPolicyApprovalConfigRequestApprovalConfig = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.approval_config = approval_config
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.region_id = region_id

    def validate(self):
        if self.approval_config:
            self.approval_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_config is not None:
            result['ApprovalConfig'] = self.approval_config.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalConfig') is not None:
            temp_model = SetPolicyApprovalConfigRequestApprovalConfig()
            self.approval_config = temp_model.from_map(m['ApprovalConfig'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetPolicyApprovalConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        approval_config_shrink: str = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.approval_config_shrink = approval_config_shrink
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_config_shrink is not None:
            result['ApprovalConfig'] = self.approval_config_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalConfig') is not None:
            self.approval_config_shrink = m.get('ApprovalConfig')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetPolicyApprovalConfigResponseBody(TeaModel):
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


class SetPolicyApprovalConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetPolicyApprovalConfigResponseBody = None,
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
            temp_model = SetPolicyApprovalConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPolicyAssetScopeRequestDatabases(TeaModel):
    def __init__(
        self,
        account_scope_type: str = None,
        database_account_ids: List[str] = None,
        database_id: str = None,
    ):
        self.account_scope_type = account_scope_type
        self.database_account_ids = database_account_ids
        self.database_id = database_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_scope_type is not None:
            result['AccountScopeType'] = self.account_scope_type
        if self.database_account_ids is not None:
            result['DatabaseAccountIds'] = self.database_account_ids
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScopeType') is not None:
            self.account_scope_type = m.get('AccountScopeType')
        if m.get('DatabaseAccountIds') is not None:
            self.database_account_ids = m.get('DatabaseAccountIds')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        return self


class SetPolicyAssetScopeRequestHostGroups(TeaModel):
    def __init__(
        self,
        account_names: List[str] = None,
        account_scope_type: str = None,
        host_group_id: str = None,
    ):
        self.account_names = account_names
        self.account_scope_type = account_scope_type
        self.host_group_id = host_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_names is not None:
            result['AccountNames'] = self.account_names
        if self.account_scope_type is not None:
            result['AccountScopeType'] = self.account_scope_type
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNames') is not None:
            self.account_names = m.get('AccountNames')
        if m.get('AccountScopeType') is not None:
            self.account_scope_type = m.get('AccountScopeType')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class SetPolicyAssetScopeRequestHosts(TeaModel):
    def __init__(
        self,
        account_scope_type: str = None,
        host_account_ids: List[str] = None,
        host_id: str = None,
    ):
        self.account_scope_type = account_scope_type
        self.host_account_ids = host_account_ids
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_scope_type is not None:
            result['AccountScopeType'] = self.account_scope_type
        if self.host_account_ids is not None:
            result['HostAccountIds'] = self.host_account_ids
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScopeType') is not None:
            self.account_scope_type = m.get('AccountScopeType')
        if m.get('HostAccountIds') is not None:
            self.host_account_ids = m.get('HostAccountIds')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class SetPolicyAssetScopeRequest(TeaModel):
    def __init__(
        self,
        databases: List[SetPolicyAssetScopeRequestDatabases] = None,
        host_groups: List[SetPolicyAssetScopeRequestHostGroups] = None,
        hosts: List[SetPolicyAssetScopeRequestHosts] = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
        scope_type: str = None,
    ):
        self.databases = databases
        self.host_groups = host_groups
        self.hosts = hosts
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.region_id = region_id
        self.scope_type = scope_type

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = SetPolicyAssetScopeRequestDatabases()
                self.databases.append(temp_model.from_map(k))
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = SetPolicyAssetScopeRequestHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = SetPolicyAssetScopeRequestHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class SetPolicyAssetScopeResponseBody(TeaModel):
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


class SetPolicyAssetScopeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetPolicyAssetScopeResponseBody = None,
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
            temp_model = SetPolicyAssetScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPolicyCommandConfigRequestCommandConfigApproval(TeaModel):
    def __init__(
        self,
        commands: List[str] = None,
    ):
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commands is not None:
            result['Commands'] = self.commands
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        return self


class SetPolicyCommandConfigRequestCommandConfigDeny(TeaModel):
    def __init__(
        self,
        acl_type: str = None,
        commands: List[str] = None,
    ):
        self.acl_type = acl_type
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.commands is not None:
            result['Commands'] = self.commands
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        return self


class SetPolicyCommandConfigRequestCommandConfig(TeaModel):
    def __init__(
        self,
        approval: SetPolicyCommandConfigRequestCommandConfigApproval = None,
        deny: SetPolicyCommandConfigRequestCommandConfigDeny = None,
    ):
        self.approval = approval
        self.deny = deny

    def validate(self):
        if self.approval:
            self.approval.validate()
        if self.deny:
            self.deny.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval is not None:
            result['Approval'] = self.approval.to_map()
        if self.deny is not None:
            result['Deny'] = self.deny.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Approval') is not None:
            temp_model = SetPolicyCommandConfigRequestCommandConfigApproval()
            self.approval = temp_model.from_map(m['Approval'])
        if m.get('Deny') is not None:
            temp_model = SetPolicyCommandConfigRequestCommandConfigDeny()
            self.deny = temp_model.from_map(m['Deny'])
        return self


class SetPolicyCommandConfigRequest(TeaModel):
    def __init__(
        self,
        command_config: SetPolicyCommandConfigRequestCommandConfig = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.command_config = command_config
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.region_id = region_id

    def validate(self):
        if self.command_config:
            self.command_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_config is not None:
            result['CommandConfig'] = self.command_config.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandConfig') is not None:
            temp_model = SetPolicyCommandConfigRequestCommandConfig()
            self.command_config = temp_model.from_map(m['CommandConfig'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetPolicyCommandConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        command_config_shrink: str = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.command_config_shrink = command_config_shrink
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_config_shrink is not None:
            result['CommandConfig'] = self.command_config_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandConfig') is not None:
            self.command_config_shrink = m.get('CommandConfig')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetPolicyCommandConfigResponseBody(TeaModel):
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


class SetPolicyCommandConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetPolicyCommandConfigResponseBody = None,
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
            temp_model = SetPolicyCommandConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPolicyIPAclConfigRequestIPAclConfig(TeaModel):
    def __init__(
        self,
        acl_type: str = None,
        ips: List[str] = None,
    ):
        self.acl_type = acl_type
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.ips is not None:
            result['IPs'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('IPs') is not None:
            self.ips = m.get('IPs')
        return self


class SetPolicyIPAclConfigRequest(TeaModel):
    def __init__(
        self,
        ipacl_config: SetPolicyIPAclConfigRequestIPAclConfig = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.ipacl_config = ipacl_config
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.region_id = region_id

    def validate(self):
        if self.ipacl_config:
            self.ipacl_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipacl_config is not None:
            result['IPAclConfig'] = self.ipacl_config.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPAclConfig') is not None:
            temp_model = SetPolicyIPAclConfigRequestIPAclConfig()
            self.ipacl_config = temp_model.from_map(m['IPAclConfig'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetPolicyIPAclConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        ipacl_config_shrink: str = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.ipacl_config_shrink = ipacl_config_shrink
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipacl_config_shrink is not None:
            result['IPAclConfig'] = self.ipacl_config_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPAclConfig') is not None:
            self.ipacl_config_shrink = m.get('IPAclConfig')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetPolicyIPAclConfigResponseBody(TeaModel):
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


class SetPolicyIPAclConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetPolicyIPAclConfigResponseBody = None,
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
            temp_model = SetPolicyIPAclConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPolicyProtocolConfigRequestProtocolConfigRDP(TeaModel):
    def __init__(
        self,
        clipboard_download: str = None,
        clipboard_upload: str = None,
        disk_redirection: str = None,
        record_keyboard: str = None,
    ):
        self.clipboard_download = clipboard_download
        self.clipboard_upload = clipboard_upload
        self.disk_redirection = disk_redirection
        self.record_keyboard = record_keyboard

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clipboard_download is not None:
            result['ClipboardDownload'] = self.clipboard_download
        if self.clipboard_upload is not None:
            result['ClipboardUpload'] = self.clipboard_upload
        if self.disk_redirection is not None:
            result['DiskRedirection'] = self.disk_redirection
        if self.record_keyboard is not None:
            result['RecordKeyboard'] = self.record_keyboard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClipboardDownload') is not None:
            self.clipboard_download = m.get('ClipboardDownload')
        if m.get('ClipboardUpload') is not None:
            self.clipboard_upload = m.get('ClipboardUpload')
        if m.get('DiskRedirection') is not None:
            self.disk_redirection = m.get('DiskRedirection')
        if m.get('RecordKeyboard') is not None:
            self.record_keyboard = m.get('RecordKeyboard')
        return self


class SetPolicyProtocolConfigRequestProtocolConfigSSH(TeaModel):
    def __init__(
        self,
        exec_command: str = None,
        sftpchannel: str = None,
        sftpdownload_file: str = None,
        sftpmkdir: str = None,
        sftpremove_file: str = None,
        sftprename_file: str = None,
        sftprmdir: str = None,
        sftpupload_file: str = None,
        sshchannel: str = None,
        x_11forwarding: str = None,
    ):
        self.exec_command = exec_command
        self.sftpchannel = sftpchannel
        self.sftpdownload_file = sftpdownload_file
        self.sftpmkdir = sftpmkdir
        self.sftpremove_file = sftpremove_file
        self.sftprename_file = sftprename_file
        self.sftprmdir = sftprmdir
        self.sftpupload_file = sftpupload_file
        self.sshchannel = sshchannel
        self.x_11forwarding = x_11forwarding

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec_command is not None:
            result['ExecCommand'] = self.exec_command
        if self.sftpchannel is not None:
            result['SFTPChannel'] = self.sftpchannel
        if self.sftpdownload_file is not None:
            result['SFTPDownloadFile'] = self.sftpdownload_file
        if self.sftpmkdir is not None:
            result['SFTPMkdir'] = self.sftpmkdir
        if self.sftpremove_file is not None:
            result['SFTPRemoveFile'] = self.sftpremove_file
        if self.sftprename_file is not None:
            result['SFTPRenameFile'] = self.sftprename_file
        if self.sftprmdir is not None:
            result['SFTPRmdir'] = self.sftprmdir
        if self.sftpupload_file is not None:
            result['SFTPUploadFile'] = self.sftpupload_file
        if self.sshchannel is not None:
            result['SSHChannel'] = self.sshchannel
        if self.x_11forwarding is not None:
            result['X11Forwarding'] = self.x_11forwarding
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecCommand') is not None:
            self.exec_command = m.get('ExecCommand')
        if m.get('SFTPChannel') is not None:
            self.sftpchannel = m.get('SFTPChannel')
        if m.get('SFTPDownloadFile') is not None:
            self.sftpdownload_file = m.get('SFTPDownloadFile')
        if m.get('SFTPMkdir') is not None:
            self.sftpmkdir = m.get('SFTPMkdir')
        if m.get('SFTPRemoveFile') is not None:
            self.sftpremove_file = m.get('SFTPRemoveFile')
        if m.get('SFTPRenameFile') is not None:
            self.sftprename_file = m.get('SFTPRenameFile')
        if m.get('SFTPRmdir') is not None:
            self.sftprmdir = m.get('SFTPRmdir')
        if m.get('SFTPUploadFile') is not None:
            self.sftpupload_file = m.get('SFTPUploadFile')
        if m.get('SSHChannel') is not None:
            self.sshchannel = m.get('SSHChannel')
        if m.get('X11Forwarding') is not None:
            self.x_11forwarding = m.get('X11Forwarding')
        return self


class SetPolicyProtocolConfigRequestProtocolConfig(TeaModel):
    def __init__(
        self,
        rdp: SetPolicyProtocolConfigRequestProtocolConfigRDP = None,
        ssh: SetPolicyProtocolConfigRequestProtocolConfigSSH = None,
    ):
        self.rdp = rdp
        self.ssh = ssh

    def validate(self):
        if self.rdp:
            self.rdp.validate()
        if self.ssh:
            self.ssh.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rdp is not None:
            result['RDP'] = self.rdp.to_map()
        if self.ssh is not None:
            result['SSH'] = self.ssh.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RDP') is not None:
            temp_model = SetPolicyProtocolConfigRequestProtocolConfigRDP()
            self.rdp = temp_model.from_map(m['RDP'])
        if m.get('SSH') is not None:
            temp_model = SetPolicyProtocolConfigRequestProtocolConfigSSH()
            self.ssh = temp_model.from_map(m['SSH'])
        return self


class SetPolicyProtocolConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        policy_id: str = None,
        protocol_config: SetPolicyProtocolConfigRequestProtocolConfig = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.protocol_config = protocol_config
        self.region_id = region_id

    def validate(self):
        if self.protocol_config:
            self.protocol_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.protocol_config is not None:
            result['ProtocolConfig'] = self.protocol_config.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('ProtocolConfig') is not None:
            temp_model = SetPolicyProtocolConfigRequestProtocolConfig()
            self.protocol_config = temp_model.from_map(m['ProtocolConfig'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetPolicyProtocolConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        policy_id: str = None,
        protocol_config_shrink: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.protocol_config_shrink = protocol_config_shrink
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
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.protocol_config_shrink is not None:
            result['ProtocolConfig'] = self.protocol_config_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('ProtocolConfig') is not None:
            self.protocol_config_shrink = m.get('ProtocolConfig')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetPolicyProtocolConfigResponseBody(TeaModel):
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


class SetPolicyProtocolConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetPolicyProtocolConfigResponseBody = None,
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
            temp_model = SetPolicyProtocolConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPolicyUserScopeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
        scope_type: str = None,
        user_group_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.region_id = region_id
        self.scope_type = scope_type
        self.user_group_ids = user_group_ids
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
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class SetPolicyUserScopeResponseBody(TeaModel):
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


class SetPolicyUserScopeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetPolicyUserScopeResponseBody = None,
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
            temp_model = SetPolicyUserScopeResponseBody()
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


class VerifyInstanceADAuthServerRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        base_dn: str = None,
        domain: str = None,
        filter: str = None,
        instance_id: str = None,
        is_ssl: str = None,
        password: str = None,
        port: str = None,
        region_id: str = None,
        server: str = None,
        standby_server: str = None,
    ):
        self.account = account
        self.base_dn = base_dn
        self.domain = domain
        self.filter = filter
        self.instance_id = instance_id
        self.is_ssl = is_ssl
        self.password = password
        self.port = port
        self.region_id = region_id
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
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl
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
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')
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


class VerifyInstanceADAuthServerResponseBody(TeaModel):
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


class VerifyInstanceADAuthServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyInstanceADAuthServerResponseBody = None,
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
            temp_model = VerifyInstanceADAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyInstanceLDAPAuthServerRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        base_dn: str = None,
        filter: str = None,
        instance_id: str = None,
        is_ssl: str = None,
        password: str = None,
        port: str = None,
        region_id: str = None,
        server: str = None,
        standby_server: str = None,
    ):
        self.account = account
        self.base_dn = base_dn
        self.filter = filter
        self.instance_id = instance_id
        self.is_ssl = is_ssl
        self.password = password
        self.port = port
        self.region_id = region_id
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
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl
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
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')
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


class VerifyInstanceLDAPAuthServerResponseBody(TeaModel):
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


class VerifyInstanceLDAPAuthServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyInstanceLDAPAuthServerResponseBody = None,
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
            temp_model = VerifyInstanceLDAPAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


