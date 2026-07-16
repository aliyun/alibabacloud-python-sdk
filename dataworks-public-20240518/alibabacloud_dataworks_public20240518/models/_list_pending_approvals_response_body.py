# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListPendingApprovalsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListPendingApprovalsResponseBodyData = None,
        request_id: str = None,
    ):
        # Paginated results.
        self.data = data
        # API request ID, generated as UUID.
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
            temp_model = main_models.ListPendingApprovalsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPendingApprovalsResponseBodyData(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListPendingApprovalsResponseBodyDataData] = None,
        has_more: bool = None,
        next_token: str = None,
        page_size: int = None,
    ):
        # Data list in the paginated results.
        self.data = data
        # Whether more data is available.
        self.has_more = has_more
        # Cursor.
        self.next_token = next_token
        # Page size (default: 10, maximum: 200).
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
                temp_model = main_models.ListPendingApprovalsResponseBodyDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListPendingApprovalsResponseBodyDataData(DaraModel):
    def __init__(
        self,
        application_time: int = None,
        contents: List[main_models.ListPendingApprovalsResponseBodyDataDataContents] = None,
        def_schema: str = None,
        process_instance_id: str = None,
        reason: str = None,
        status: str = None,
    ):
        # Time when the request was submitted.
        self.application_time = application_time
        # Request content.
        self.contents = contents
        # Resource type.
        self.def_schema = def_schema
        # Process instance ID.
        self.process_instance_id = process_instance_id
        # Reason for the request.
        self.reason = reason
        # Approval status. Enumeration:
        # 
        # - WaitApproval: Pending approval
        # - Confirmed: Pending authorization
        # - RejectApproval: Approval rejected
        # - AuthorizeSucceed: Authorization succeeded
        # - AuthorizeFailed: Authorization failed
        # - Deleted: Deleted
        # - Canceled: Canceled
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
                temp_model = main_models.ListPendingApprovalsResponseBodyDataDataContents()
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

class ListPendingApprovalsResponseBodyDataDataContents(DaraModel):
    def __init__(
        self,
        access_types: List[str] = None,
        auth_method: str = None,
        create_time: int = None,
        def_schema: str = None,
        expiration_time: int = None,
        final_access_types: List[str] = None,
        grantee: main_models.ListPendingApprovalsResponseBodyDataDataContentsGrantee = None,
        id: str = None,
        process_instance_id: str = None,
        resource: main_models.ListPendingApprovalsResponseBodyDataDataContentsResource = None,
        resource_name: str = None,
        status: str = None,
        tenant_id: str = None,
        update_time: int = None,
    ):
        # Resource operation permissions requested in the application.
        self.access_types = access_types
        # Authorization method.
        self.auth_method = auth_method
        # Creation time.
        self.create_time = create_time
        # Resource type.
        self.def_schema = def_schema
        # Permission expiration date, millisecond timestamp.
        self.expiration_time = expiration_time
        # Resource operation permissions finally approved.
        self.final_access_types = final_access_types
        # Authorization principal description.
        self.grantee = grantee
        # Unique identifier of the request content.
        self.id = id
        # **Process instance ID.**
        self.process_instance_id = process_instance_id
        # Resource declaration.
        self.resource = resource
        # Minimum permission resource type.
        self.resource_name = resource_name
        # Approval status. Enumeration:
        # 
        # - WaitApproval: Pending approval
        # - Confirmed: Pending authorization
        # - RejectApproval: Approval rejected
        # - AuthorizeSucceed: Authorization succeeded
        # - AuthorizeFailed: Authorization failed
        # - Deleted: Deleted
        # - Canceled: Canceled
        self.status = status
        # Tenant ID.
        self.tenant_id = tenant_id
        # Update time.
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
            temp_model = main_models.ListPendingApprovalsResponseBodyDataDataContentsGrantee()
            self.grantee = temp_model.from_map(m.get('Grantee'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('Resource') is not None:
            temp_model = main_models.ListPendingApprovalsResponseBodyDataDataContentsResource()
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

class ListPendingApprovalsResponseBodyDataDataContentsResource(DaraModel):
    def __init__(
        self,
        def_schema: str = None,
        def_version: str = None,
        meta_data: Dict[str, Any] = None,
    ):
        # ResourceSchema.name that the resource parsing depends on.
        self.def_schema = def_schema
        # ResourceSchema.version that the resource parsing depends on.
        self.def_version = def_version
        # Resource metadata. The data content is constrained by ResourceSchema.
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

class ListPendingApprovalsResponseBodyDataDataContentsGrantee(DaraModel):
    def __init__(
        self,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # Principal ID.
        # 
        # Note: The semantics of the ID vary depending on the principalType:
        # - RamUser: DataWorks UserId
        # - RamRole: DataWorks UserId prefixed with "ROLE_"
        # - DataworksTenantMember: DataWorks UserId
        # - DataworksTenantRole: DataWorks tenant roleCode
        # - DataworksProjectRole: DataWorks workspace roleCode
        # - DataworksProjectMember: DataWorks UserId
        # - DlfRole: DlfNext role name
        self.principal_id = principal_id
        # Principal type. Enumeration:
        # 
        # - RamRole
        # - RamUser
        # - DataworksTenantMember
        # - DataworksTenantRole
        # - DataworksProjectMember
        # - DataworksProjectRole
        # - DlfRole
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

