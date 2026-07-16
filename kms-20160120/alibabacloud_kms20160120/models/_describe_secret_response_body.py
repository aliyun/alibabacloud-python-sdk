# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kms20160120 import models as main_models
from darabonba.model import DaraModel

class DescribeSecretResponseBody(DaraModel):
    def __init__(
        self,
        arn: str = None,
        automatic_rotation: str = None,
        create_time: str = None,
        dkmsinstance_id: str = None,
        description: str = None,
        encryption_key_id: str = None,
        extended_config: str = None,
        last_rotation_date: str = None,
        next_rotation_date: str = None,
        owing_service: str = None,
        planned_delete_time: str = None,
        request_id: str = None,
        rotation_interval: str = None,
        secret_name: str = None,
        secret_type: str = None,
        tags: main_models.DescribeSecretResponseBodyTags = None,
        update_time: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the secret.
        self.arn = arn
        # Indicates whether automatic rotation is enabled. Valid values:
        # 
        # *   Enabled: indicates that automatic rotation is enabled.
        # *   Disabled: indicates that automatic rotation is disabled.
        # *   Invalid: indicates that the status of automatic rotation is abnormal. In this case, Secrets Manager cannot automatically rotate the secret.
        # 
        # >  This parameter is returned only for a managed ApsaraDB RDS secret, a managed RAM secret, or a managed ECS secret.
        self.automatic_rotation = automatic_rotation
        # The time when the secret was created.
        self.create_time = create_time
        # The ID of the dedicated KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The description of the secret.
        self.description = description
        # The ID of the customer master key (CMK) that is used to encrypt the secret value.
        self.encryption_key_id = encryption_key_id
        # The extended configuration of the secret.
        # 
        # >  This parameter is returned only for a managed ApsaraDB RDS secret, a managed Resource Access Management (RAM) secret, or a managed Elastic Compute Service (ECS) secret.
        self.extended_config = extended_config
        # The time when the last rotation was performed.
        # 
        # >  This parameter is returned if the secret was rotated.
        self.last_rotation_date = last_rotation_date
        # The time when the next rotation will be performed.
        # 
        # >  This parameter is returned when automatic rotation is enabled.
        self.next_rotation_date = next_rotation_date
        self.owing_service = owing_service
        # The time when the secret is scheduled to be deleted.
        self.planned_delete_time = planned_delete_time
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The interval for automatic rotation.
        # 
        # The value is in the `integer[unit]` format. `integer` indicates the length of time. `unit`: indicates the time unit. The value of `unit` is fixed as s. For example, if the value is 604800s, automatic rotation is performed at a 7-day interval.
        # 
        # >  This parameter is returned when automatic rotation is enabled.
        self.rotation_interval = rotation_interval
        # The name of the secret.
        self.secret_name = secret_name
        # The type of the secret. Valid values:
        # 
        # *   Generic: indicates a generic secret.
        # *   Rds: indicates a managed ApsaraDB RDS secret.
        # *   RAMCredentials: indicates a managed RAM secret.
        # *   ECS: indicates a managed ECS secret.
        self.secret_type = secret_type
        self.tags = tags
        # The time when the secret was updated.
        self.update_time = update_time

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id

        if self.description is not None:
            result['Description'] = self.description

        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id

        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config

        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date

        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date

        if self.owing_service is not None:
            result['OwingService'] = self.owing_service

        if self.planned_delete_time is not None:
            result['PlannedDeleteTime'] = self.planned_delete_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.secret_type is not None:
            result['SecretType'] = self.secret_type

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')

        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')

        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')

        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')

        if m.get('OwingService') is not None:
            self.owing_service = m.get('OwingService')

        if m.get('PlannedDeleteTime') is not None:
            self.planned_delete_time = m.get('PlannedDeleteTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeSecretResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeSecretResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeSecretResponseBodyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeSecretResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeSecretResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

