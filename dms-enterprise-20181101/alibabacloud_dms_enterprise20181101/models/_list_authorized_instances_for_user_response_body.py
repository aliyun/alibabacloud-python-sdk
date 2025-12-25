# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizedInstancesForUserResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListAuthorizedInstancesForUserResponseBodyInstances] = None,
        request_id: str = None,
    ):
        # The list of instances on which the user has permissions.
        self.instances = instances
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListAuthorizedInstancesForUserResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAuthorizedInstancesForUserResponseBodyInstances(DaraModel):
    def __init__(
        self,
        db_type: str = None,
        env_type: str = None,
        host: str = None,
        instance_alias: str = None,
        instance_id: str = None,
        permission_detail: main_models.ListAuthorizedInstancesForUserResponseBodyInstancesPermissionDetail = None,
        port: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The database engine that the instance runs.
        self.db_type = db_type
        # The type of the environment to which the database instance belongs.
        self.env_type = env_type
        # The endpoint that is used to connect to the instance.
        self.host = host
        # The alias of the instance.
        self.instance_alias = instance_alias
        # The ID of the instance.
        self.instance_id = instance_id
        # The details of permissions. The format of the permission details varies with the permission source. For example, if the permission source is a normal permission, the following parameters are returned.
        self.permission_detail = permission_detail
        # The port number that is used to connect to the instance.
        self.port = port
        # The user IDs.
        self.user_id = user_id
        # The user name.
        self.user_name = user_name

    def validate(self):
        if self.permission_detail:
            self.permission_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.permission_detail is not None:
            result['PermissionDetail'] = self.permission_detail.to_map()

        if self.port is not None:
            result['Port'] = self.port

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PermissionDetail') is not None:
            temp_model = main_models.ListAuthorizedInstancesForUserResponseBodyInstancesPermissionDetail()
            self.permission_detail = temp_model.from_map(m.get('PermissionDetail'))

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class ListAuthorizedInstancesForUserResponseBodyInstancesPermissionDetail(DaraModel):
    def __init__(
        self,
        ds_type: str = None,
        expire_date: str = None,
        message: str = None,
        perm_type: str = None,
    ):
        # The type of object on which the operation is performed.
        self.ds_type = ds_type
        # The time when the permission expires.
        self.expire_date = expire_date
        # If the permission source is a permission policy, the value of this parameter includes the policy name and the operations that are allowed for the user.
        self.message = message
        # The type of the permission. Valid values:
        # 
        # *   **QUERY**: the query permission
        # *   **EXPORT**: the data export permission
        # *   **CORRECT**: the data change permission
        self.perm_type = perm_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds_type is not None:
            result['DsType'] = self.ds_type

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.message is not None:
            result['Message'] = self.message

        if self.perm_type is not None:
            result['PermType'] = self.perm_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')

        return self

