# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetApplicationContentsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetApplicationContentsResponseBodyData = None,
        request_id: str = None,
    ):
        # The process instance and its associated application contents.
        self.data = data
        # The request ID. Use this ID to locate logs and troubleshoot issues.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetApplicationContentsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationContentsResponseBodyData(DaraModel):
    def __init__(
        self,
        application_time: int = None,
        contents: List[main_models.GetApplicationContentsResponseBodyDataContents] = None,
        def_schema: str = None,
        process_instance_id: str = None,
        reason: str = None,
        status: str = None,
    ):
        # The time when the application was submitted. This value is a millisecond-precision timestamp.
        self.application_time = application_time
        # A list of the application contents.
        self.contents = contents
        # The resource type.
        self.def_schema = def_schema
        # The process instance ID.
        self.process_instance_id = process_instance_id
        # The reason for the application.
        self.reason = reason
        # The approval status. Valid values:
        # 
        # - `WaitApproval`: The application is pending approval.
        # 
        # - `Confirmed`: The application is pending authorization.
        # 
        # - `RejectApproval`: The application was rejected.
        # 
        # - `AuthorizeSucceed`: Authorization was successful.
        # 
        # - `AuthorizeFailed`: Authorization failed.
        # 
        # - `Deleted`: The application was deleted.
        # 
        # - `Canceled`: The application was canceled.
        self.status = status

    def validate(self):
        if self.contents:
            for v1 in self.contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_time is not None:
            result['ApplicationTime'] = self.application_time

        result['Contents'] = []
        if self.contents is not None:
            for k1 in self.contents:
                result['Contents'].append(k1.to_map() if k1 else None)

        if self.def_schema is not None:
            result['DefSchema'] = self.def_schema

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationTime') is not None:
            self.application_time = m.get('ApplicationTime')

        self.contents = []
        if m.get('Contents') is not None:
            for k1 in m.get('Contents'):
                temp_model = main_models.GetApplicationContentsResponseBodyDataContents()
                self.contents.append(temp_model.from_map(k1))

        if m.get('DefSchema') is not None:
            self.def_schema = m.get('DefSchema')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetApplicationContentsResponseBodyDataContents(DaraModel):
    def __init__(
        self,
        access_types: List[str] = None,
        auth_method: str = None,
        create_time: int = None,
        def_schema: str = None,
        expiration_time: int = None,
        final_access_types: List[str] = None,
        grantee: main_models.GetApplicationContentsResponseBodyDataContentsGrantee = None,
        id: str = None,
        process_instance_id: str = None,
        resource: main_models.GetApplicationContentsResponseBodyDataContentsResource = None,
        resource_name: str = None,
        status: str = None,
        tenant_id: str = None,
        update_time: int = None,
    ):
        # A list of the permissions requested for the resource.
        self.access_types = access_types
        # The authorization method.
        self.auth_method = auth_method
        # The time when the content item was created. This value is a millisecond-precision timestamp.
        self.create_time = create_time
        # The resource type.
        self.def_schema = def_schema
        # The time when the permissions expire. This value is a millisecond-precision timestamp.
        self.expiration_time = expiration_time
        # A list of the permissions granted in the final approval.
        self.final_access_types = final_access_types
        # The grantee.
        self.grantee = grantee
        # The unique ID of the application content item.
        self.id = id
        # The ID of the approval process instance for the application.
        self.process_instance_id = process_instance_id
        # The resource declaration.
        self.resource = resource
        # The specific type of the resource, such as a table.
        self.resource_name = resource_name
        # The approval status. Valid values:
        # 
        # - `WaitApproval`: The item is pending approval.
        # 
        # - `Confirmed`: The item is pending authorization.
        # 
        # - `RejectApproval`: The item was rejected.
        # 
        # - `AuthorizeSucceed`: Authorization was successful.
        # 
        # - `AuthorizeFailed`: Authorization failed.
        # 
        # - `Deleted`: The item was deleted during the approval process.
        # 
        # - `Canceled`: The item was canceled.
        self.status = status
        # The tenant ID.
        self.tenant_id = tenant_id
        # The time when the content item was last updated. This value is a millisecond-precision timestamp.
        self.update_time = update_time

    def validate(self):
        if self.grantee:
            self.grantee.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_types is not None:
            result['AccessTypes'] = self.access_types

        if self.auth_method is not None:
            result['AuthMethod'] = self.auth_method

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.def_schema is not None:
            result['DefSchema'] = self.def_schema

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.final_access_types is not None:
            result['FinalAccessTypes'] = self.final_access_types

        if self.grantee is not None:
            result['Grantee'] = self.grantee.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTypes') is not None:
            self.access_types = m.get('AccessTypes')

        if m.get('AuthMethod') is not None:
            self.auth_method = m.get('AuthMethod')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefSchema') is not None:
            self.def_schema = m.get('DefSchema')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('FinalAccessTypes') is not None:
            self.final_access_types = m.get('FinalAccessTypes')

        if m.get('Grantee') is not None:
            temp_model = main_models.GetApplicationContentsResponseBodyDataContentsGrantee()
            self.grantee = temp_model.from_map(m.get('Grantee'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('Resource') is not None:
            temp_model = main_models.GetApplicationContentsResponseBodyDataContentsResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetApplicationContentsResponseBodyDataContentsResource(DaraModel):
    def __init__(
        self,
        def_schema: str = None,
        def_version: str = None,
        meta_data: str = None,
    ):
        # The name of the `ResourceSchema` that defines how to parse this resource.
        self.def_schema = def_schema
        # The version of the `ResourceSchema` that defines how to parse this resource.
        self.def_version = def_version
        # The resource metadata. The structure of the metadata is defined by the `ResourceSchema`.
        self.meta_data = meta_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.def_schema is not None:
            result['DefSchema'] = self.def_schema

        if self.def_version is not None:
            result['DefVersion'] = self.def_version

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefSchema') is not None:
            self.def_schema = m.get('DefSchema')

        if m.get('DefVersion') is not None:
            self.def_version = m.get('DefVersion')

        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        return self

class GetApplicationContentsResponseBodyDataContentsGrantee(DaraModel):
    def __init__(
        self,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # The ID of the principal. The format of the ID varies based on the `PrincipalType` value:
        # 
        # - If `PrincipalType` is `RamUser`, this parameter specifies the ID of a DataWorks user.
        # 
        # - If `PrincipalType` is `RamRole`, this parameter specifies the ID of a role in DataWorks. The ID must be prefixed with `ROLE_`.
        # 
        # - If `PrincipalType` is `DlfRole`, this parameter specifies the name of a DlfNext role.
        self.principal_id = principal_id
        # The principal type. Valid values:
        # 
        # - `RamUser`
        # 
        # - `RamRole`
        # 
        # - `DlfRole`
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

