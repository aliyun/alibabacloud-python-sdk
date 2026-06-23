# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListMyApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListMyApplicationsResponseBodyData = None,
        request_id: str = None,
    ):
        # The paginated results.
        self.data = data
        # A unique identifier (UUID) generated for the request.
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
            temp_model = main_models.ListMyApplicationsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMyApplicationsResponseBodyData(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListMyApplicationsResponseBodyDataData] = None,
        has_more: bool = None,
        next_token: str = None,
        page_size: int = None,
    ):
        # The list of application details.
        self.data = data
        # Indicates whether more results are available.
        self.has_more = has_more
        # The cursor to retrieve the next page of results. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The page size. Default value: 10. Maximum value: 200.
        self.page_size = page_size

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListMyApplicationsResponseBodyDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListMyApplicationsResponseBodyDataData(DaraModel):
    def __init__(
        self,
        application_time: int = None,
        contents: List[main_models.ListMyApplicationsResponseBodyDataDataContents] = None,
        def_schema: str = None,
        process_instance_id: str = None,
        reason: str = None,
        status: str = None,
    ):
        # The time the application was submitted, in Unix timestamp format (milliseconds).
        self.application_time = application_time
        # The content of the application.
        self.contents = contents
        # The resource type.
        self.def_schema = def_schema
        # The process instance ID.
        self.process_instance_id = process_instance_id
        # The reason for the application.
        self.reason = reason
        # The approval status. Valid values:
        # 
        # - `WaitApproval`: Pending approval
        # 
        # - `Confirmed`: Pending authorization
        # 
        # - `RejectApproval`: Rejected
        # 
        # - `AuthorizeSucceed`: Authorization succeeded
        # 
        # - `AuthorizeFailed`: Authorization failed
        # 
        # - `Deleted`: Deleted
        # 
        # - `Canceled`: Canceled
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
                temp_model = main_models.ListMyApplicationsResponseBodyDataDataContents()
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

class ListMyApplicationsResponseBodyDataDataContents(DaraModel):
    def __init__(
        self,
        access_types: List[str] = None,
        auth_method: str = None,
        create_time: int = None,
        def_schema: str = None,
        expiration_time: int = None,
        final_access_types: List[str] = None,
        grantee: main_models.ListMyApplicationsResponseBodyDataDataContentsGrantee = None,
        id: str = None,
        process_instance_id: str = None,
        resource: main_models.ListMyApplicationsResponseBodyDataDataContentsResource = None,
        resource_name: str = None,
        status: str = None,
        tenant_id: str = None,
        update_time: int = None,
    ):
        # The permissions requested for the resource.
        self.access_types = access_types
        # The authorization method.
        self.auth_method = auth_method
        # The time when the item was created, in Unix timestamp format (milliseconds).
        self.create_time = create_time
        # The resource type.
        self.def_schema = def_schema
        # When the permission expires, in Unix timestamp format (milliseconds).
        self.expiration_time = expiration_time
        # The granted permissions.
        self.final_access_types = final_access_types
        # **The principal to be granted the permission.**
        self.grantee = grantee
        # The unique ID of the application item.
        self.id = id
        # The ID of the approval process instance for the application.
        self.process_instance_id = process_instance_id
        # **The requested resource.**
        self.resource = resource
        # The category of the resource. For example, `table`.
        self.resource_name = resource_name
        # The approval status. Valid values:
        # 
        # - `WaitApproval`: Pending approval
        # 
        # - `Confirmed`: Pending authorization
        # 
        # - `RejectApproval`: Rejected
        # 
        # - `AuthorizeSucceed`: Authorization succeeded
        # 
        # - `AuthorizeFailed`: Authorization failed
        # 
        # - `Deleted`: Deleted
        # 
        # - `Canceled`: Canceled
        self.status = status
        # The tenant ID.
        self.tenant_id = tenant_id
        # The time when the item was last updated, in Unix timestamp format (milliseconds).
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
            temp_model = main_models.ListMyApplicationsResponseBodyDataDataContentsGrantee()
            self.grantee = temp_model.from_map(m.get('Grantee'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('Resource') is not None:
            temp_model = main_models.ListMyApplicationsResponseBodyDataDataContentsResource()
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

class ListMyApplicationsResponseBodyDataDataContentsResource(DaraModel):
    def __init__(
        self,
        def_schema: str = None,
        def_version: str = None,
        meta_data: Dict[str, Any] = None,
    ):
        # **The name of the `ResourceSchema` used to parse the resource.**
        self.def_schema = def_schema
        # **The version of the `ResourceSchema` used to parse the resource.**
        self.def_version = def_version
        # **The resource metadata. Its format is defined by the `ResourceSchema`.**
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

class ListMyApplicationsResponseBodyDataDataContentsGrantee(DaraModel):
    def __init__(
        self,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # The ID of the principal. The value of this parameter varies based on the value of `PrincipalType`:
        # 
        # - `RamUser`: The DataWorks user ID.
        # 
        # - `RamRole`: The DataWorks user ID, prefixed with `ROLE_`.
        # 
        # - `DataworksTenantMember`: The DataWorks user ID.
        # 
        # - `DataworksTenantRole`: The DataWorks tenant role code.
        # 
        # - `DataworksProjectRole`: The DataWorks workspace role code.
        # 
        # - `DataworksProjectMember`: The DataWorks user ID.
        # 
        # - `DlfRole`: The DlfNext role name.
        self.principal_id = principal_id
        # The type of the principal. Valid values:
        # 
        # - `RamRole`
        # 
        # - `RamUser`
        # 
        # - `DataworksTenantMember`
        # 
        # - `DataworksTenantRole`
        # 
        # - `DataworksProjectMember`
        # 
        # - `DataworksProjectRole`
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

