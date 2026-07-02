# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_kms20160120 import models as main_models
from darabonba.model import DaraModel

class DescribeKeyResponseBody(DaraModel):
    def __init__(
        self,
        key_metadata: main_models.DescribeKeyResponseBodyKeyMetadata = None,
        request_id: str = None,
    ):
        # The metadata of the CMK.
        self.key_metadata = key_metadata
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.key_metadata:
            self.key_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_metadata is not None:
            result['KeyMetadata'] = self.key_metadata.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyMetadata') is not None:
            temp_model = main_models.DescribeKeyResponseBodyKeyMetadata()
            self.key_metadata = temp_model.from_map(m.get('KeyMetadata'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeKeyResponseBodyKeyMetadata(DaraModel):
    def __init__(
        self,
        arn: str = None,
        automatic_rotation: str = None,
        creation_date: str = None,
        creator: str = None,
        dkmsinstance_id: str = None,
        delete_date: str = None,
        deletion_protection: str = None,
        deletion_protection_description: str = None,
        description: str = None,
        key_id: str = None,
        key_spec: str = None,
        key_state: str = None,
        key_usage: str = None,
        last_rotation_date: str = None,
        material_expire_time: str = None,
        next_rotation_date: str = None,
        origin: str = None,
        primary_key_version: str = None,
        protection_level: str = None,
        rotation_interval: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the CMK.
        self.arn = arn
        # Indicates whether automatic key rotation is enabled. Valid values:
        # 
        # - Enabled
        # 
        # - Disabled
        # 
        # - Suspended
        # 
        # For more information, see [Automatic key rotation](https://help.aliyun.com/document_detail/134270.html).
        # 
        # > Only symmetric CMKs support automatic key rotation.
        self.automatic_rotation = automatic_rotation
        # The time when the CMK was created. The time is displayed in UTC.
        self.creation_date = creation_date
        # The Alibaba Cloud account that is used to create the CMK.
        self.creator = creator
        # The ID of the dedicated KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The time at which the CMK is scheduled for deletion. The time is displayed in UTC.
        # 
        # For more information, see [ScheduleKeyDeletion](https://help.aliyun.com/document_detail/44196.html).
        # 
        # > This parameter is returned only when the value of the KeyState parameter is PendingDeletion.
        self.delete_date = delete_date
        # Indicates whether deletion protection is enabled. Valid values:
        # 
        # - Enabled
        # 
        # - Disabled
        self.deletion_protection = deletion_protection
        # The description of deletion protection.
        self.deletion_protection_description = deletion_protection_description
        # The description of the CMK.
        self.description = description
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id
        # The type of the CMK.
        self.key_spec = key_spec
        # The status of the CMK.
        # 
        # For more information, see [Impact of CMK status on API operations](https://help.aliyun.com/document_detail/44211.html).
        self.key_state = key_state
        # The usage of the CMK.
        self.key_usage = key_usage
        # The time when the last rotation was performed. The time is displayed in UTC. For a new CMK, the value of this parameter is the time when the initial version of the CMK was generated.
        self.last_rotation_date = last_rotation_date
        # The time when the key material expires. The time is displayed in UTC. If this parameter value is empty, the key material does not expire.
        self.material_expire_time = material_expire_time
        # The time when the next rotation will be performed.
        # 
        # > This parameter is returned only when the value of the AutomaticRotation parameter is Enabled or Suspended.
        self.next_rotation_date = next_rotation_date
        # The source of the key material for the CMK.
        self.origin = origin
        # The ID of the current primary key version for the symmetric CMK.
        self.primary_key_version = primary_key_version
        # The protection level of the CMK.
        self.protection_level = protection_level
        # The interval for automatic key rotation.
        # 
        # Unit: seconds.
        # 
        # For example, if the value is 604800s, automatic key rotation is performed at a 7-day interval.
        # 
        # > This parameter is returned only when the value of the AutomaticRotation parameter is Enabled or Suspended.
        self.rotation_interval = rotation_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation

        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id

        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deletion_protection_description is not None:
            result['DeletionProtectionDescription'] = self.deletion_protection_description

        if self.description is not None:
            result['Description'] = self.description

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec

        if self.key_state is not None:
            result['KeyState'] = self.key_state

        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage

        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date

        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time

        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.primary_key_version is not None:
            result['PrimaryKeyVersion'] = self.primary_key_version

        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level

        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')

        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')

        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeletionProtectionDescription') is not None:
            self.deletion_protection_description = m.get('DeletionProtectionDescription')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')

        if m.get('KeyState') is not None:
            self.key_state = m.get('KeyState')

        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')

        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')

        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')

        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('PrimaryKeyVersion') is not None:
            self.primary_key_version = m.get('PrimaryKeyVersion')

        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')

        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')

        return self

