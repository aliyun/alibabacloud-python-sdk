# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListCloudAccountResourcesForCloudPermissionTemplateResponseBody(DaraModel):
    def __init__(
        self,
        cloud_account_resources: List[main_models.ListCloudAccountResourcesForCloudPermissionTemplateResponseBodyCloudAccountResources] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of cloud account resources.
        self.cloud_account_resources = cloud_account_resources
        # The number of entries per page in a paging query.
        self.max_results = max_results
        # The query token returned by the current call. Use this token for the next paginated query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries in the list.
        self.total_count = total_count

    def validate(self):
        if self.cloud_account_resources:
            for v1 in self.cloud_account_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudAccountResources'] = []
        if self.cloud_account_resources is not None:
            for k1 in self.cloud_account_resources:
                result['CloudAccountResources'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_account_resources = []
        if m.get('CloudAccountResources') is not None:
            for k1 in m.get('CloudAccountResources'):
                temp_model = main_models.ListCloudAccountResourcesForCloudPermissionTemplateResponseBodyCloudAccountResources()
                self.cloud_account_resources.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCloudAccountResourcesForCloudPermissionTemplateResponseBodyCloudAccountResources(DaraModel):
    def __init__(
        self,
        cloud_account_id: str = None,
        cloud_account_resource_entity_id: str = None,
        cloud_account_resource_entity_type: str = None,
        cloud_account_resource_id: str = None,
        cloud_account_resource_meta: main_models.ListCloudAccountResourcesForCloudPermissionTemplateResponseBodyCloudAccountResourcesCloudAccountResourceMeta = None,
        cloud_account_resource_name: str = None,
        create_time: int = None,
        description: str = None,
        update_time: int = None,
    ):
        # The ID of the cloud account to which the resource belongs.
        self.cloud_account_id = cloud_account_id
        # The resource entity identifier, which is a unique remote identifier.
        self.cloud_account_resource_entity_id = cloud_account_resource_entity_id
        # The resource entity type. Valid values: ram_role.
        self.cloud_account_resource_entity_type = cloud_account_resource_entity_type
        # The identifier of the cloud account resource.
        self.cloud_account_resource_id = cloud_account_resource_id
        # The resource metadata.
        self.cloud_account_resource_meta = cloud_account_resource_meta
        # The name of the resource.
        self.cloud_account_resource_name = cloud_account_resource_name
        # The creation time. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The description.
        self.description = description
        # The last update time. The value is a UNIX timestamp in milliseconds.
        self.update_time = update_time

    def validate(self):
        if self.cloud_account_resource_meta:
            self.cloud_account_resource_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        if self.cloud_account_resource_entity_id is not None:
            result['CloudAccountResourceEntityId'] = self.cloud_account_resource_entity_id

        if self.cloud_account_resource_entity_type is not None:
            result['CloudAccountResourceEntityType'] = self.cloud_account_resource_entity_type

        if self.cloud_account_resource_id is not None:
            result['CloudAccountResourceId'] = self.cloud_account_resource_id

        if self.cloud_account_resource_meta is not None:
            result['CloudAccountResourceMeta'] = self.cloud_account_resource_meta.to_map()

        if self.cloud_account_resource_name is not None:
            result['CloudAccountResourceName'] = self.cloud_account_resource_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        if m.get('CloudAccountResourceEntityId') is not None:
            self.cloud_account_resource_entity_id = m.get('CloudAccountResourceEntityId')

        if m.get('CloudAccountResourceEntityType') is not None:
            self.cloud_account_resource_entity_type = m.get('CloudAccountResourceEntityType')

        if m.get('CloudAccountResourceId') is not None:
            self.cloud_account_resource_id = m.get('CloudAccountResourceId')

        if m.get('CloudAccountResourceMeta') is not None:
            temp_model = main_models.ListCloudAccountResourcesForCloudPermissionTemplateResponseBodyCloudAccountResourcesCloudAccountResourceMeta()
            self.cloud_account_resource_meta = temp_model.from_map(m.get('CloudAccountResourceMeta'))

        if m.get('CloudAccountResourceName') is not None:
            self.cloud_account_resource_name = m.get('CloudAccountResourceName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListCloudAccountResourcesForCloudPermissionTemplateResponseBodyCloudAccountResourcesCloudAccountResourceMeta(DaraModel):
    def __init__(
        self,
        cam_policy_document: str = None,
        cam_policy_type: str = None,
        iam_policy_document: str = None,
        iam_policy_type: str = None,
        ram_policy_document: str = None,
        ram_policy_type: str = None,
    ):
        # The JSON string of the Tencent Cloud CAM policy document. This parameter is returned only for Tencent Cloud accounts.
        self.cam_policy_document = cam_policy_document
        # The Tencent Cloud CAM policy type. Valid values: qcs and local. This parameter is returned only for Tencent Cloud accounts.
        self.cam_policy_type = cam_policy_type
        # The JSON string of the AWS IAM policy document. This parameter is returned only for AWS cloud accounts.
        self.iam_policy_document = iam_policy_document
        # The AWS IAM policy type. Valid values: aws and local. This parameter is returned only for AWS cloud accounts.
        self.iam_policy_type = iam_policy_type
        # The JSON string of the RAM policy document. This parameter is returned only by the get operation.
        self.ram_policy_document = ram_policy_document
        # The RAM policy type. Valid values: system and custom.
        self.ram_policy_type = ram_policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cam_policy_document is not None:
            result['CamPolicyDocument'] = self.cam_policy_document

        if self.cam_policy_type is not None:
            result['CamPolicyType'] = self.cam_policy_type

        if self.iam_policy_document is not None:
            result['IamPolicyDocument'] = self.iam_policy_document

        if self.iam_policy_type is not None:
            result['IamPolicyType'] = self.iam_policy_type

        if self.ram_policy_document is not None:
            result['RamPolicyDocument'] = self.ram_policy_document

        if self.ram_policy_type is not None:
            result['RamPolicyType'] = self.ram_policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CamPolicyDocument') is not None:
            self.cam_policy_document = m.get('CamPolicyDocument')

        if m.get('CamPolicyType') is not None:
            self.cam_policy_type = m.get('CamPolicyType')

        if m.get('IamPolicyDocument') is not None:
            self.iam_policy_document = m.get('IamPolicyDocument')

        if m.get('IamPolicyType') is not None:
            self.iam_policy_type = m.get('IamPolicyType')

        if m.get('RamPolicyDocument') is not None:
            self.ram_policy_document = m.get('RamPolicyDocument')

        if m.get('RamPolicyType') is not None:
            self.ram_policy_type = m.get('RamPolicyType')

        return self

