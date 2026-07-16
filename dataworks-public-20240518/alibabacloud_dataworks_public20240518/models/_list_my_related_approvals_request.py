# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListMyRelatedApprovalsRequest(DaraModel):
    def __init__(
        self,
        access_types: List[str] = None,
        def_schema: str = None,
        end_time: int = None,
        grantee: main_models.ListMyRelatedApprovalsRequestGrantee = None,
        next_token: str = None,
        page_size: int = None,
        resource: main_models.ListMyRelatedApprovalsRequestResource = None,
        resource_type: List[str] = None,
        start_time: int = None,
        statuses: List[str] = None,
    ):
        # Filter by requested permissions.
        # 
        # Note: Different resource levels support different application permission types, all constrained by [ResourceSchema](https://help.aliyun.com/zh/dataworks/developer-reference/resourceschema-template-instructions).isValidLeaf, accessTypeRestrictions, and authMethodAccessTypes.
        # 
        # Reference: [ResourceSchema International Site Documentation](https://www.alibabacloud.com/help/zh/dataworks/developer-reference/resourceschema-template-instructions)
        self.access_types = access_types
        # Filter by resource type.
        # 
        # Note: The resource types supported by the system for applications are constrained by [ResourceSchema](https://help.aliyun.com/zh/dataworks/developer-reference/resourceschema-template-instructions).name.
        # 
        # Reference: [ResourceSchema International Site Documentation](https://www.alibabacloud.com/help/zh/dataworks/developer-reference/resourceschema-template-instructions)
        # 
        # This parameter is required.
        self.def_schema = def_schema
        # Application time end (millisecond timestamp)
        self.end_time = end_time
        # Filter by authorization principal.
        # 
        # Note: The authorization principal types supported by the system are constrained by [ResourceSchema](https://help.aliyun.com/zh/dataworks/developer-reference/resourceschema-template-instructions).authPrincipal.
        # 
        # Reference: [ResourceSchema International Site Documentation](https://www.alibabacloud.com/help/zh/dataworks/developer-reference/resourceschema-template-instructions)
        self.grantee = grantee
        # Pagination cursor
        self.next_token = next_token
        # Page size (default 10, maximum 200)
        self.page_size = page_size
        # Filter by resource with exact/generalized matching. The resource description is constrained by [ResourceSchema](https://help.aliyun.com/zh/dataworks/developer-reference/resourceschema-template-instructions).
        # 
        # Reference: [ResourceSchema International Site Documentation](https://www.alibabacloud.com/help/zh/dataworks/developer-reference/resourceschema-template-instructions)
        self.resource = resource
        # Filter by minimum permission resource type.
        # 
        # Note: The minimum permission resource type is constrained by [ResourceSchema](https://help.aliyun.com/zh/dataworks/developer-reference/resourceschema-template-instructions).resources[*].isValidLeaf being true.
        # 
        # Reference: [ResourceSchema International Site Documentation](https://www.alibabacloud.com/help/zh/dataworks/developer-reference/resourceschema-template-instructions)
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # Application time start (millisecond timestamp)
        self.start_time = start_time
        # Filter by approval status. Enum values:
        # 
        # - WaitApproval: Pending approval
        # - Confirmed: Pending authorization
        # - RejectApproval: Approval rejected
        # - AuthorizeSucceed: Authorization succeeded
        # - AuthorizeFailed: Authorization failed
        # - Deleted: Deleted
        # - Canceled: Withdrawn
        self.statuses = statuses

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

        if self.def_schema is not None:
            result['DefSchema'] = self.def_schema

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.grantee is not None:
            result['Grantee'] = self.grantee.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTypes') is not None:
            self.access_types = m.get('AccessTypes')

        if m.get('DefSchema') is not None:
            self.def_schema = m.get('DefSchema')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Grantee') is not None:
            temp_model = main_models.ListMyRelatedApprovalsRequestGrantee()
            self.grantee = temp_model.from_map(m.get('Grantee'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Resource') is not None:
            temp_model = main_models.ListMyRelatedApprovalsRequestResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

class ListMyRelatedApprovalsRequestResource(DaraModel):
    def __init__(
        self,
        def_schema: str = None,
        def_version: str = None,
        meta_data: Dict[str, Any] = None,
    ):
        # Resource type.
        # 
        # Note: The resource types supported by the system for applications are constrained by [ResourceSchema](https://help.aliyun.com/zh/dataworks/developer-reference/resourceschema-template-instructions).name.
        # 
        # Reference: [ResourceSchema International Site Documentation](https://www.alibabacloud.com/help/zh/dataworks/developer-reference/resourceschema-template-instructions)
        self.def_schema = def_schema
        # The resource parsing version is constrained by [ResourceSchema](https://help.aliyun.com/zh/dataworks/developer-reference/resourceschema-template-instructions).version.
        # 
        # [ResourceSchema International Site Documentation](https://www.alibabacloud.com/help/zh/dataworks/developer-reference/resourceschema-template-instructions)
        self.def_version = def_version
        # Resource metadata.
        # 
        # Note: The metadata is constrained by [ResourceSchema](https://help.aliyun.com/zh/dataworks/developer-reference/resourceschema-template-instructions).resources. A valid resource declaration must include the full-path metadata declaration from level 0 to validLeaf layer.
        # 
        # Reference: [ResourceSchema International Site Documentation](https://www.alibabacloud.com/help/zh/dataworks/developer-reference/resourceschema-template-instructions)
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

class ListMyRelatedApprovalsRequestGrantee(DaraModel):
    def __init__(
        self,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # Authorization principal ID:
        # 
        # - `RamUser`: Dataworks UserId
        # - `RamRole`: Dataworks UserId prefixed with "ROLE_"
        # - `DataworksTenantMember`: Dataworks UserId
        # - `DataworksTenantRole`: Dataworks tenant roleCode
        # - `DataworksProjectRole`: Dataworks workspace roleCode
        # - `DataworksProjectMember`: Dataworks UserId
        # - `DlfRole`: DlfNext role name
        self.principal_id = principal_id
        # Authorization principal type:
        # 
        # - `RamRole`
        # - `RamUser`
        # - `DataworksTenantMember`
        # - `DataworksTenantRole`
        # - `DataworksProjectMember`
        # - `DataworksProjectRole`
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

