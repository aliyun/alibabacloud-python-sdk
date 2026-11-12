# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetCloudAccountResourceResponseBody(DaraModel):
    def __init__(
        self,
        cloud_account_resource: main_models.GetCloudAccountResourceResponseBodyCloudAccountResource = None,
        request_id: str = None,
    ):
        # The cloud account resource information.
        self.cloud_account_resource = cloud_account_resource
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cloud_account_resource:
            self.cloud_account_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_resource is not None:
            result['CloudAccountResource'] = self.cloud_account_resource.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudAccountResource') is not None:
            temp_model = main_models.GetCloudAccountResourceResponseBodyCloudAccountResource()
            self.cloud_account_resource = temp_model.from_map(m.get('CloudAccountResource'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCloudAccountResourceResponseBodyCloudAccountResource(DaraModel):
    def __init__(
        self,
        cloud_account_id: str = None,
        cloud_account_resource_entity_id: str = None,
        cloud_account_resource_entity_type: str = None,
        cloud_account_resource_id: str = None,
        cloud_account_resource_meta: main_models.GetCloudAccountResourceResponseBodyCloudAccountResourceCloudAccountResourceMeta = None,
        cloud_account_resource_name: str = None,
        create_time: int = None,
        description: str = None,
        update_time: int = None,
    ):
        # The cloud account ID.
        self.cloud_account_id = cloud_account_id
        # The unique remote identifier of the resource entity.
        self.cloud_account_resource_entity_id = cloud_account_resource_entity_id
        # The resource entity type. Valid values: ram_policy.
        self.cloud_account_resource_entity_type = cloud_account_resource_entity_type
        # The cloud account resource ID.
        self.cloud_account_resource_id = cloud_account_resource_id
        # The resource metadata information.
        self.cloud_account_resource_meta = cloud_account_resource_meta
        # The resource name.
        self.cloud_account_resource_name = cloud_account_resource_name
        # The creation time. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The description.
        self.description = description
        # The update time.
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
            temp_model = main_models.GetCloudAccountResourceResponseBodyCloudAccountResourceCloudAccountResourceMeta()
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

class GetCloudAccountResourceResponseBodyCloudAccountResourceCloudAccountResourceMeta(DaraModel):
    def __init__(
        self,
        cam_policy_document: str = None,
        cam_policy_type: str = None,
        iam_policy_document: str = None,
        iam_policy_type: str = None,
        ram_policy_document: str = None,
        ram_policy_type: str = None,
    ):
        # The Tencent Cloud CAM policy document in JSON format. This parameter is returned only for Tencent Cloud accounts.
        self.cam_policy_document = cam_policy_document
        # The Tencent Cloud CAM policy type. Valid values: qcs and local. This parameter is returned only for Tencent Cloud accounts.
        self.cam_policy_type = cam_policy_type
        # The AWS IAM policy document in JSON format. This parameter is returned only for AWS cloud accounts.
        self.iam_policy_document = iam_policy_document
        # The AWS IAM policy type. Valid values: aws and local. This parameter is returned only for AWS cloud accounts.
        self.iam_policy_type = iam_policy_type
        # The RAM policy document in JSON format. This parameter is returned only by the Get operation.
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

