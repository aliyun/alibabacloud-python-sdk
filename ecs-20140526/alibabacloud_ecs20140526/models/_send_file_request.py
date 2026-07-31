# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class SendFileRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        content: str = None,
        content_type: str = None,
        description: str = None,
        file_group: str = None,
        file_mode: str = None,
        file_owner: str = None,
        instance_id: List[str] = None,
        name: str = None,
        overwrite: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.SendFileRequestTag] = None,
        target_dir: str = None,
        timeout: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. **ClientToken** supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The content of the file. The file content cannot exceed 32 KB after Base64 encoding.
        # 
        # - If `ContentType` is set to `PlainText`, this parameter specifies the plain text content.
        # - If `ContentType` is set to `Base64`, this parameter specifies the Base64-encoded content.
        # 
        # This parameter is required.
        self.content = content
        # The content type of the file. Valid values:
        # - PlainText: plain text.
        # - Base64: Base64-encoded.
        # 
        # Default value: PlainText.
        self.content_type = content_type
        # The description of the file. The full character set is supported. The description cannot exceed 512 characters in length.
        self.description = description
        # The group of the file. This parameter takes effect only on Linux instances. Default value: root. The value cannot exceed 64 characters in length.
        # 
        # > If you specify a different user group, make sure that the user group exists on the instance.
        self.file_group = file_group
        # The permissions on the file. This parameter takes effect only on Linux instances. You can configure this parameter in the same way as you run the chmod command.
        # 
        # Default value: 0644, which indicates that the owner has read and write permissions, and the group and other users have read-only permissions.
        self.file_mode = file_mode
        # The owner of the file. This parameter takes effect only on Linux instances. Default value: root. The value cannot exceed 64 characters in length.
        # 
        # > If you specify a different user, make sure that the user exists on the instance.
        self.file_owner = file_owner
        # The IDs of the ECS instances to which you want to send the file. You can specify up to 50 instance IDs. Valid values of N: 1 to 50.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the file. The full character set is supported. The name cannot exceed 255 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether to overwrite a file with the same name in the destination directory. Valid values:
        # - true: Overwrite the file.
        # - false: Do not overwrite the file.
        # 
        # Default value: false.
        self.overwrite = overwrite
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the target ECS instances. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group for file sending. If you specify this parameter:
        # 
        # - The ECS instances specified by InstanceId must belong to this resource group.
        # 
        # - You can filter file sending results by specifying this parameter when you call [DescribeSendFileResults](https://help.aliyun.com/document_detail/184117.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        self.tag = tag
        # The destination directory on the target ECS instances where the file is sent. If the directory does not exist, it is automatically created. The directory path cannot exceed 255 characters in length.
        # 
        # This parameter is required.
        self.target_dir = target_dir
        # The timeout period for sending the file. Unit: seconds.
        # 
        # - A timeout may occur when the file cannot be sent due to a process issue, a missing module, or a missing Cloud Assistant Agent.
        # - If the specified timeout period is less than 10 seconds, the system automatically sets the timeout period to 10 seconds to ensure successful delivery.
        # 
        # Default value: 60.
        self.timeout = timeout

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content is not None:
            result['Content'] = self.content

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.description is not None:
            result['Description'] = self.description

        if self.file_group is not None:
            result['FileGroup'] = self.file_group

        if self.file_mode is not None:
            result['FileMode'] = self.file_mode

        if self.file_owner is not None:
            result['FileOwner'] = self.file_owner

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.target_dir is not None:
            result['TargetDir'] = self.target_dir

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileGroup') is not None:
            self.file_group = m.get('FileGroup')

        if m.get('FileMode') is not None:
            self.file_mode = m.get('FileMode')

        if m.get('FileOwner') is not None:
            self.file_owner = m.get('FileOwner')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.SendFileRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TargetDir') is not None:
            self.target_dir = m.get('TargetDir')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class SendFileRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag for file sending. Valid values of N: 1 to 20. The tag key cannot be an empty string.
        # 
        # If you use a single tag to filter resources, the resource count with this tag cannot exceed 1,000. If you use multiple tags to filter resources, the resource count with all the specified tags attached cannot exceed 1,000. If the resource count exceeds 1,000, call [ListTagResources](https://help.aliyun.com/document_detail/110425.html) to query the resources.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag for file sending. Valid values of N: 1 to 20. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

