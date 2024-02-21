# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CancelTaskRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyImageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        destination_region_id: str = None,
        image_id: str = None,
        image_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see How to ensure idempotence.
        self.client_token = client_token
        # The image description. The description must be 2 to 256 characters in length but cannot start with http:// or https://.
        self.description = description
        # The destination region to which you want to copy the image.
        self.destination_region_id = destination_region_id
        # The ID of the image that you want to copy.
        self.image_id = image_id
        # The image name. The name must be 2 to 128 characters in length. The name can contain letters, digits, colons (:), underscores (\_), and hyphens (-). The name can contain letters, digits, colons (:), underscores (\_), and hyphens (-). It must start with a letter but cannot start with http:// or https://.
        self.image_name = image_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The source region from which you want to copy the image.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CopyImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        # The ID of the image that is copied to the destination region.
        self.image_id = image_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CopyImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        image_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see How to ensure idempotence.
        self.client_token = client_token
        # The image description. The description must be 2 to 256 characters in length. It cannot start with `http://` or `https://`.
        self.description = description
        # The image name. The name must be 2 to 128 characters in length. It can contain letters, digits, colons (:), underscores (\_), and hyphens (-). The name must start with a letter but cannot start with `http://` or `https://`.
        self.image_name = image_name
        # The instance ID.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        # The custom image ID.
        self.image_id = image_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImagesRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
        image_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to forcefully delete the image. Default value: false
        self.force = force
        # The image IDs. You can specify up to 100 images.
        self.image_id = image_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteImagesResponseBodyImageResponsesImageResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        image_id: str = None,
        message: str = None,
    ):
        # The HTTP status code that is returned when the image is deleted.
        self.code = code
        # The ID of the image that is requested for deletion.
        self.image_id = image_id
        # The message that is returned when the image is deleted.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteImagesResponseBodyImageResponses(TeaModel):
    def __init__(
        self,
        image_response: List[DeleteImagesResponseBodyImageResponsesImageResponse] = None,
    ):
        self.image_response = image_response

    def validate(self):
        if self.image_response:
            for k in self.image_response:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageResponse'] = []
        if self.image_response is not None:
            for k in self.image_response:
                result['ImageResponse'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_response = []
        if m.get('ImageResponse') is not None:
            for k in m.get('ImageResponse'):
                temp_model = DeleteImagesResponseBodyImageResponsesImageResponse()
                self.image_response.append(temp_model.from_map(k))
        return self


class DeleteImagesResponseBody(TeaModel):
    def __init__(
        self,
        image_responses: DeleteImagesResponseBodyImageResponses = None,
        request_id: str = None,
    ):
        # Details about images that are deleted.
        self.image_responses = image_responses
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.image_responses:
            self.image_responses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_responses is not None:
            result['ImageResponses'] = self.image_responses.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageResponses') is not None:
            temp_model = DeleteImagesResponseBodyImageResponses()
            self.image_responses = temp_model.from_map(m['ImageResponses'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteImagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstancesRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to forcefully release the instance if it is in the Running status. Valid values:
        # 
        # *   true. If you set the Force parameter to true, temporary data in the memory and storage of the instance is erased and cannot be restored after you call the operation, which is similar to the effect of a power-off action.
        # *   false (default)
        self.force = force
        # The instance IDs. Valid values of N: 1 to 100.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeyPairsRequest(TeaModel):
    def __init__(
        self,
        key_pair_name: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The name of the key pair that the cloud phone uses. The value can be a JSON array that consists of up to 100 SSH key pair names. Separate multiple key pair names with commas (,).
        self.key_pair_name = key_pair_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the key pair that you want to delete.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteKeyPairsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteKeyPairsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteKeyPairsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteKeyPairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchFileRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        oss_bucket: str = None,
        oss_object: str = None,
        owner_account: str = None,
        owner_id: int = None,
        path: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the instance on which you want to run the command. Valid values of N: 1 to 10.
        self.instance_id = instance_id
        # The OSS bucket to which the file that you want to upload.
        # 
        # >  Before you import an APK file to the OSS bucket for the first time, add a Resource Access Management (RAM) policy. Otherwise, NoSetRoletoECSServiceAcount appears.
        self.oss_bucket = oss_bucket
        # The name that you want to save to OSS.
        self.oss_object = oss_object
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The path in which you want to store the file in the cloud phone.
        self.path = path
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_object is not None:
            result['OssObject'] = self.oss_object
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class FetchFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class FetchFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FetchFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FetchFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportImageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        format: str = None,
        image_name: str = None,
        oss_bucket: str = None,
        oss_object: str = None,
        owner_account: str = None,
        owner_id: int = None,
        platform: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The image description. The description must be 2 to 256 characters in length, and cannot start with `http://` or `https://`.
        self.description = description
        # The image format. Valid values:
        # 
        # *   RAW
        # *   QCOW2
        self.format = format
        # The image name. The name must be 2 to 128 characters in length. The name can contain letters, digits, colons (:), underscores (\_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        self.image_name = image_name
        # The OSS bucket to which you want to import the image.
        self.oss_bucket = oss_bucket
        # The name (key) of the image file that you want to use as an OSS object.
        self.oss_object = oss_object
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The OS distribution. Valid values:
        # 
        # *   Android 9.0
        self.platform = platform
        # The ID of the region where you want to import the image to the ECP instance.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.format is not None:
            result['Format'] = self.format
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_object is not None:
            result['OssObject'] = self.oss_object
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ImportImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        # The ID of the image that is imported to the instance.
        self.image_id = image_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ImportImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportKeyPairRequest(TeaModel):
    def __init__(
        self,
        key_pair_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        public_key_body: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The name of the key pair. The name must be globally unique. The name must be 2 to 128 characters in length. The name must start with a letter but cannot start with http:// or https://. The name can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.key_pair_name = key_pair_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The public key of the key pair.
        self.public_key_body = public_key_body
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.public_key_body is not None:
            result['PublicKeyBody'] = self.public_key_body
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PublicKeyBody') is not None:
            self.public_key_body = m.get('PublicKeyBody')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ImportKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        key_pair_finger_print: str = None,
        key_pair_name: str = None,
        request_id: str = None,
    ):
        # The fingerprint of the key pair. The message-digest algorithm 5 (MD5) is used based on the public key fingerprint format defined in RFC 4716.
        self.key_pair_finger_print = key_pair_finger_print
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportKeyPairResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ImportKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallApplicationRequest(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        oss_bucket: str = None,
        oss_object: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The IDs of the instances on which you want to run the command. Valid values of N: 1 to 10.
        self.instance_id = instance_id
        # The Object Storage Service (OSS) bucket in which you want to store the application file.
        # 
        # >  Before you import application files to the OSS bucket for the first time, add a Resource Access Management (RAM) policy. Otherwise, NoSetRoletoECSServiceAcount appears.
        self.oss_bucket = oss_bucket
        # The name (key) of the application file that is used as an OSS object.
        self.oss_object = oss_object
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_object is not None:
            result['OssObject'] = self.oss_object
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class InstallApplicationResponseBodyTaskId(TeaModel):
    def __init__(
        self,
        task_id: List[str] = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class InstallApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: InstallApplicationResponseBodyTaskId = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task IDs.
        self.task_id = task_id

    def validate(self):
        if self.task_id:
            self.task_id.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            temp_model = InstallApplicationResponseBodyTaskId()
            self.task_id = temp_model.from_map(m['TaskId'])
        return self


class InstallApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InstallApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImageSharePermissionRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the image that you want to import to the instance.
        self.image_id = image_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListImageSharePermissionResponseBodyAccountsAccount(TeaModel):
    def __init__(
        self,
        aliyun_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.aliyun_id = aliyun_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        return self


class ListImageSharePermissionResponseBodyAccounts(TeaModel):
    def __init__(
        self,
        account: List[ListImageSharePermissionResponseBodyAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = ListImageSharePermissionResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class ListImageSharePermissionResponseBody(TeaModel):
    def __init__(
        self,
        accounts: ListImageSharePermissionResponseBodyAccounts = None,
        request_id: str = None,
    ):
        # The list of Alibaba Cloud accounts.
        self.accounts = accounts
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = ListImageSharePermissionResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListImageSharePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImageSharePermissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListImageSharePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        image_category: str = None,
        image_id: List[str] = None,
        image_name: str = None,
        instance_type: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        # The image source. Valid values:
        # 
        # *   system: public images provided by Alibaba Cloud.
        # *   self: custom images that you create.
        # *   others: shared images from other Alibaba Cloud accounts.
        self.image_category = image_category
        # The image IDs. Valid values of N: 1 to 100.
        self.image_id = image_id
        # The image name. The name must be 2 to 128 characters in length. It can contain letters, digits, colons (:), underscores (\_), and hyphens (-). The name must start with a letter but cannot start with `http://` or `https://`.
        self.image_name = image_name
        # The instance type.
        self.instance_type = instance_type
        # The maximum number of entries to return on each page. Valid values: 1 to 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The image state. Valid values:
        # 
        # *   Waiting
        # *   Creating
        # *   Copying
        # *   Importing
        # *   Available (default)
        # *   CreateFailed
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListImagesResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        image_category: str = None,
        image_id: str = None,
        image_name: str = None,
        is_self_shared: bool = None,
        osname: str = None,
        osname_en: str = None,
        ostype: str = None,
        platform: str = None,
        progress: str = None,
        status: str = None,
        usage: str = None,
    ):
        # The time when the image was created. The time follows the ISO 8601 standard.
        self.creation_time = creation_time
        # The image description.
        self.description = description
        # The image type.
        self.image_category = image_category
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # Indicates whether the image is shared with other Alibaba Cloud accounts.
        self.is_self_shared = is_self_shared
        # The display name of the OS in Chinese.
        self.osname = osname
        # The display name of the OS in English.
        self.osname_en = osname_en
        # The image OS.
        self.ostype = ostype
        # The OS distribution.
        self.platform = platform
        # The progress of image creation.
        self.progress = progress
        # The image state.
        self.status = status
        # Indicates whether the image is used by instances. Valid values:
        # 
        # *   none: The image is idle.
        # *   instance: The image is used by instances.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.is_self_shared is not None:
            result['IsSelfShared'] = self.is_self_shared
        if self.osname is not None:
            result['OSName'] = self.osname
        if self.osname_en is not None:
            result['OSNameEn'] = self.osname_en
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('IsSelfShared') is not None:
            self.is_self_shared = m.get('IsSelfShared')
        if m.get('OSName') is not None:
            self.osname = m.get('OSName')
        if m.get('OSNameEn') is not None:
            self.osname_en = m.get('OSNameEn')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class ListImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[ListImagesResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = ListImagesResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(
        self,
        images: ListImagesResponseBodyImages = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of images.
        self.images = images
        # The maximum number of entries that is returned on each page. Valid values: 1 to 100.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The total number of images.
        self.total_count = total_count

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.images is not None:
            result['Images'] = self.images.to_map()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Images') is not None:
            temp_model = ListImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceTypesRequest(TeaModel):
    def __init__(
        self,
        instance_type: List[str] = None,
        instance_type_family: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The names of the instance types. Valid values of N: 1 to 100.
        self.instance_type = instance_type
        # The instance type family.
        self.instance_type_family = instance_type_family
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListInstanceTypesResponseBodyInstanceTypesInstanceTypeResolutions(TeaModel):
    def __init__(
        self,
        resolution: List[str] = None,
    ):
        self.resolution = resolution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        return self


class ListInstanceTypesResponseBodyInstanceTypesInstanceType(TeaModel):
    def __init__(
        self,
        cpu_core_count: int = None,
        default_resolution: str = None,
        instance_type: str = None,
        instance_type_family: str = None,
        memory_size: str = None,
        name: str = None,
        name_en: str = None,
        resolutions: ListInstanceTypesResponseBodyInstanceTypesInstanceTypeResolutions = None,
    ):
        # The number of vCPUs supported by the instance type.
        self.cpu_core_count = cpu_core_count
        # The default resolution supported by the instance type.
        self.default_resolution = default_resolution
        # The instance type.
        self.instance_type = instance_type
        # The instance type family.
        self.instance_type_family = instance_type_family
        # The memory size supported by the instance type. Unit: GiB.
        self.memory_size = memory_size
        # The name of the instance type in Chinese.
        self.name = name
        # The name of the instance type in English.
        self.name_en = name_en
        # The resolutions supported by the instance type.
        self.resolutions = resolutions

    def validate(self):
        if self.resolutions:
            self.resolutions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count
        if self.default_resolution is not None:
            result['DefaultResolution'] = self.default_resolution
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.name is not None:
            result['Name'] = self.name
        if self.name_en is not None:
            result['NameEn'] = self.name_en
        if self.resolutions is not None:
            result['Resolutions'] = self.resolutions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')
        if m.get('DefaultResolution') is not None:
            self.default_resolution = m.get('DefaultResolution')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')
        if m.get('Resolutions') is not None:
            temp_model = ListInstanceTypesResponseBodyInstanceTypesInstanceTypeResolutions()
            self.resolutions = temp_model.from_map(m['Resolutions'])
        return self


class ListInstanceTypesResponseBodyInstanceTypes(TeaModel):
    def __init__(
        self,
        instance_type: List[ListInstanceTypesResponseBodyInstanceTypesInstanceType] = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type:
            for k in self.instance_type:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceType'] = []
        if self.instance_type is not None:
            for k in self.instance_type:
                result['InstanceType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type = []
        if m.get('InstanceType') is not None:
            for k in m.get('InstanceType'):
                temp_model = ListInstanceTypesResponseBodyInstanceTypesInstanceType()
                self.instance_type.append(temp_model.from_map(k))
        return self


class ListInstanceTypesResponseBody(TeaModel):
    def __init__(
        self,
        instance_types: ListInstanceTypesResponseBodyInstanceTypes = None,
        request_id: str = None,
    ):
        # The instance types.
        self.instance_types = instance_types
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_types:
            self.instance_types.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypes') is not None:
            temp_model = ListInstanceTypesResponseBodyInstanceTypes()
            self.instance_types = temp_model.from_map(m['InstanceTypes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstanceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceTypesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstanceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceVncUrlRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the instance resides.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListInstanceVncUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vnc_url: str = None,
        web_rtc_token: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The Virtual Network Computing (VNC) connection URL.
        self.vnc_url = vnc_url
        # The token that is used for WebRTC logon.
        self.web_rtc_token = web_rtc_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vnc_url is not None:
            result['VncUrl'] = self.vnc_url
        if self.web_rtc_token is not None:
            result['WebRtcToken'] = self.web_rtc_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VncUrl') is not None:
            self.vnc_url = m.get('VncUrl')
        if m.get('WebRtcToken') is not None:
            self.web_rtc_token = m.get('WebRtcToken')
        return self


class ListInstanceVncUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceVncUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstanceVncUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance. Valid values of N: 1 to 20.
        self.key = key
        # The tag value of the instance. Valid values of N: 1 to 20.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        filter: List[ListInstancesRequestFilter] = None,
        image_id: str = None,
        instance_id: List[str] = None,
        instance_name: str = None,
        instance_type: str = None,
        key_pair_name: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resolution: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        show_web_rtc_token: bool = None,
        status: str = None,
        tag: List[ListInstancesRequestTag] = None,
        zone_id: str = None,
    ):
        # The billing method. Valid values:
        # 
        # *   PrePaid: subscription
        # *   PostPaid: pay-as-you-go
        self.charge_type = charge_type
        self.filter = filter
        # The image ID.
        self.image_id = image_id
        # The instance IDs. Valid values of N: 1 to 100.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The instance type.
        self.instance_type = instance_type
        # The key pair name. The name must be globally unique. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with http:// or https://. The name can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.key_pair_name = key_pair_name
        # The maximum number of entries returned on each page. Valid values: 1 to 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The instance resolution.
        self.resolution = resolution
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether webRtcToken is returned in the query result.
        self.show_web_rtc_token = show_web_rtc_token
        # The instance status. Valid values:
        # 
        # *   Pending: The instance is being created.
        # *   Running: The instance is running.
        # *   Starting: The instance is being started.
        # *   Stopping: The instance is being stopped.
        # *   Stopped: The instance is stopped.
        # *   Expired: The instance has expired.
        self.status = status
        # The instances that you want to filter by using a specified tag.
        self.tag = tag
        # The ID of the zone where the instance resides.
        self.zone_id = zone_id

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.show_web_rtc_token is not None:
            result['ShowWebRtcToken'] = self.show_web_rtc_token
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListInstancesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ShowWebRtcToken') is not None:
            self.show_web_rtc_token = m.get('ShowWebRtcToken')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListInstancesResponseBodyInstancesInstanceEipAddress(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        bandwidth: int = None,
        internet_charge_type: str = None,
        ip_address: str = None,
    ):
        # The ID of the EIP that is used by the instance.
        self.allocation_id = allocation_id
        # The bandwidth of the EIP.
        self.bandwidth = bandwidth
        # The billing method of the EIP.
        self.internet_charge_type = internet_charge_type
        # The EIP.
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        return self


class ListInstancesResponseBodyInstancesInstanceTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance.
        self.key = key
        # The tag value of the instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListInstancesResponseBodyInstancesInstanceTags(TeaModel):
    def __init__(
        self,
        tag: List[ListInstancesResponseBodyInstancesInstanceTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListInstancesResponseBodyInstancesInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListInstancesResponseBodyInstancesInstanceVpcAttributes(TeaModel):
    def __init__(
        self,
        private_ip_address: str = None,
        v_switch_id: str = None,
    ):
        # The private IP address.
        self.private_ip_address = private_ip_address
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class ListInstancesResponseBodyInstancesInstance(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        charge_type: str = None,
        creation_time: str = None,
        description: str = None,
        eip_address: ListInstancesResponseBodyInstancesInstanceEipAddress = None,
        expired_time: str = None,
        image_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        key_pair_name: str = None,
        os_name: str = None,
        os_name_en: str = None,
        region_id: str = None,
        resolution: str = None,
        security_group_id: str = None,
        status: str = None,
        tags: ListInstancesResponseBodyInstancesInstanceTags = None,
        vpc_attributes: ListInstancesResponseBodyInstancesInstanceVpcAttributes = None,
        web_rtc_token: str = None,
        zone_id: str = None,
    ):
        # Indicates whether auto-renewal is enabled. This parameter takes effect only for subscription instances.
        self.auto_renew = auto_renew
        # The billing method of the instance.
        self.charge_type = charge_type
        # The time when the image was created. The time follows the ISO 8601 standard.
        self.creation_time = creation_time
        # The instance description.
        self.description = description
        # The information about the elastic IP address (EIP) of the instance.
        self.eip_address = eip_address
        # The time when the subscription instance expires.
        self.expired_time = expired_time
        # The image ID.
        self.image_id = image_id
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The instance type.
        self.instance_type = instance_type
        # The name of the key pair for the instance.
        self.key_pair_name = key_pair_name
        # The display name of the OS in Chinese.
        self.os_name = os_name
        # The display name of the OS in English.
        self.os_name_en = os_name_en
        # The region ID.
        self.region_id = region_id
        # The resolution of the instance.
        self.resolution = resolution
        # The ID of the security group that the instance uses. The security group is the same as that of the Elastic Compute Service (ECS) instance that you use.
        self.security_group_id = security_group_id
        # The instance state. Valid values:
        # 
        # *   Pending: The instance is being created.
        # *   Running: The instance is running.
        # *   Starting: The instance is being started.
        # *   Stopping: The instance is being stopped.
        # *   Stopped: The instance is stopped.
        self.status = status
        # The tags of the instance.
        self.tags = tags
        # The information about the virtual private cloud (VPC) in which the instance is deployed.
        self.vpc_attributes = vpc_attributes
        # The information about webRtcToken.
        self.web_rtc_token = web_rtc_token
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.eip_address:
            self.eip_address.validate()
        if self.tags:
            self.tags.validate()
        if self.vpc_attributes:
            self.vpc_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address.to_map()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.os_name is not None:
            result['OsName'] = self.os_name
        if self.os_name_en is not None:
            result['OsNameEn'] = self.os_name_en
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.vpc_attributes is not None:
            result['VpcAttributes'] = self.vpc_attributes.to_map()
        if self.web_rtc_token is not None:
            result['WebRtcToken'] = self.web_rtc_token
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EipAddress') is not None:
            temp_model = ListInstancesResponseBodyInstancesInstanceEipAddress()
            self.eip_address = temp_model.from_map(m['EipAddress'])
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')
        if m.get('OsNameEn') is not None:
            self.os_name_en = m.get('OsNameEn')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = ListInstancesResponseBodyInstancesInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VpcAttributes') is not None:
            temp_model = ListInstancesResponseBodyInstancesInstanceVpcAttributes()
            self.vpc_attributes = temp_model.from_map(m['VpcAttributes'])
        if m.get('WebRtcToken') is not None:
            self.web_rtc_token = m.get('WebRtcToken')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        instance: List[ListInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = ListInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: ListInstancesResponseBodyInstances = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of the instances.
        self.instances = instances
        # The maximum number of entries returned on each page. Valid values: 1 to 100.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries that is returned.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
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
        if m.get('Instances') is not None:
            temp_model = ListInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKeyPairsRequest(TeaModel):
    def __init__(
        self,
        key_pair_finger_print: str = None,
        key_pair_name: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The fingerprint of the key pair. The message-digest algorithm 5 (MD5) is used based on the public key fingerprint format defined in RFC 4716.
        self.key_pair_finger_print = key_pair_finger_print
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The maximum number of entries per page. Valid values: 1 to 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the key pair resides.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListKeyPairsResponseBodyKeyPairsKeyPair(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        key_pair_finger_print: str = None,
        key_pair_name: str = None,
    ):
        # The time when the key pair was created.
        self.creation_time = creation_time
        # The fingerprint of the key pair.
        self.key_pair_finger_print = key_pair_finger_print
        # The name of the SSH key pair.
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        return self


class ListKeyPairsResponseBodyKeyPairs(TeaModel):
    def __init__(
        self,
        key_pair: List[ListKeyPairsResponseBodyKeyPairsKeyPair] = None,
    ):
        self.key_pair = key_pair

    def validate(self):
        if self.key_pair:
            for k in self.key_pair:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyPair'] = []
        if self.key_pair is not None:
            for k in self.key_pair:
                result['KeyPair'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_pair = []
        if m.get('KeyPair') is not None:
            for k in m.get('KeyPair'):
                temp_model = ListKeyPairsResponseBodyKeyPairsKeyPair()
                self.key_pair.append(temp_model.from_map(k))
        return self


class ListKeyPairsResponseBody(TeaModel):
    def __init__(
        self,
        key_pairs: ListKeyPairsResponseBodyKeyPairs = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The key pairs that are returned.
        self.key_pairs = key_pairs
        # The maximum number of entries per page. Valid values: 1 to 100.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of key pairs.
        self.total_count = total_count

    def validate(self):
        if self.key_pairs:
            self.key_pairs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pairs is not None:
            result['KeyPairs'] = self.key_pairs.to_map()
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
        if m.get('KeyPairs') is not None:
            temp_model = ListKeyPairsResponseBodyKeyPairs()
            self.key_pairs = temp_model.from_map(m['KeyPairs'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListKeyPairsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListKeyPairsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListKeyPairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # The endpoint that corresponds to the region.
        self.region_endpoint = region_endpoint
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[ListRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = ListRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: ListRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        # The details of the regions.
        self.regions = regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = ListRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_type: str = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The resource type. Valid value:
        # 
        # *   instance: Elastic Cloud Phone (ECP) instance
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBodyKeys(TeaModel):
    def __init__(
        self,
        key: List[str] = None,
    ):
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        keys: ListTagKeysResponseBodyKeys = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The tag keys.
        self.keys = keys
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. If the NextToken parameter is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.keys:
            self.keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            temp_model = ListTagKeysResponseBodyKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The resource IDs. You can specify up to 50 resources.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        # The resource type. Valid value:
        # 
        # *   instance: Elastic Cloud Phone (ECP) instance
        self.resource_type = resource_type
        # The tags. You can specify up to 20 tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The resource ID.
        self.resource_id = resource_id
        # The resource type. Valid value:
        # 
        # *   instance: ECP instance
        self.resource_type = resource_type
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. If the NextToken parameter is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of resources.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_type: str = None,
    ):
        # The tag key whose values you want to query.
        self.key = key
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The resource type. Valid value:
        # 
        # *   instance: Elastic Cloud Phone (ECP) instance
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagValuesResponseBodyValues(TeaModel):
    def __init__(
        self,
        value: List[str] = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        values: ListTagValuesResponseBodyValues = None,
    ):
        # The maximum number of entries that is returned on each page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. If the NextToken parameter is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of resources.
        self.values = values

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Values') is not None:
            temp_model = ListTagValuesResponseBodyValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagValuesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: List[str] = None,
        task_status: str = None,
        task_type: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The maximum number of entries to return on each page. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task IDs. Valid values of N: 1 to 100.
        self.task_id = task_id
        # The task state. Valid values:
        # 
        # *   Finished
        # *   Processing
        # *   Failed
        # 
        # This parameter is empty by default.
        # 
        # >  The system only queries tasks that are in the Finished, Processing, and Failed states and ignores other values.
        self.task_status = task_status
        # The name of the operation that you can call to execute the task on the instance. Valid values:
        # 
        # *   Shell: runs a shell command.
        # *   InstallApplication: installs an application.
        # *   UninstallApplication: uninstalls an application.
        # *   SendFile: uploads a file.
        # *   ImportImage: imports an image.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListTasksResponseBodyTasksTask(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        execute_msg: str = None,
        finished_time: str = None,
        instance_id: str = None,
        progress: str = None,
        task_id: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The content that is returned after the task is executed. The content can be up to 1,024 bytes in length.
        self.execute_msg = execute_msg
        # The time when the task ended.
        self.finished_time = finished_time
        # The instance ID.
        self.instance_id = instance_id
        # The task progress.
        self.progress = progress
        # The task ID.
        self.task_id = task_id
        # The task state.
        self.task_status = task_status
        # The task type.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.execute_msg is not None:
            result['ExecuteMsg'] = self.execute_msg
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExecuteMsg') is not None:
            self.execute_msg = m.get('ExecuteMsg')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        task: List[ListTasksResponseBodyTasksTask] = None,
    ):
        self.task = task

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k in m.get('Task'):
                temp_model = ListTasksResponseBodyTasksTask()
                self.task.append(temp_model.from_map(k))
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        request_id: str = None,
        tasks: ListTasksResponseBodyTasks = None,
        total_count: int = None,
    ):
        # The maximum number of entries that is returned on each page. Valid values: 1 to 200. Default value: 50.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The tasks.
        self.tasks = tasks
        # The total number of tasks.
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tasks') is not None:
            temp_model = ListTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListZonesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListZonesResponseBodyZonesZone(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone: List[ListZonesResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = ListZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class ListZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: ListZonesResponseBodyZones = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The zones available in the current region.
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Zones') is not None:
            temp_model = ListZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class ListZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListZonesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootInstancesRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to forcefully restart the instance. Valid values:
        # 
        # *   true If you set this parameter to true, cache data that is not written to storage in the instance will be lost after you call this operation, which is similar to the effect of a power-off action.
        # *   false (default)
        self.force = force
        # The instance IDs.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RebootInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebootInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebootInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RebootInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstancesRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        client_token: str = None,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to enable auto-payment. Default value: true.
        self.auto_pay = auto_pay
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see How to ensure idempotence.
        self.client_token = client_token
        # The IDs of the instances that you want to renew. You can renew up to 20 instances at a time.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The renewal period. Default value: 1.
        self.period = period
        # The unit of the renewal period.
        # 
        # *   Valid values if you set this parameter to Year: 1, 2, 3, 4, and 5.
        # *   Valid values if you set this parameter to Month (default): 1, 2, 3, and 6.
        # *   Valid values if you set this parameter to Hour: 1.
        self.period_unit = period_unit
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RenewInstancesResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RenewInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: RenewInstancesResponseBodyInstanceIds = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The IDs of the instances that are renewed.
        self.instance_ids = instance_ids
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            temp_model = RenewInstancesResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenewInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetInstancesRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The image ID of the instance. If you do not specify this parameter, the image of the current instance is used to reset the instance.
        self.image_id = image_id
        # The instance IDs. Valid values of N: 1 to 100.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ResetInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCommandRequest(TeaModel):
    def __init__(
        self,
        command: str = None,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The command that you want to run.\
        # The name can be up to 1024 bytes in length and can contain only letters, digits, underscores (\_), periods (.), slashes (/), colons (:), and hyphens (-).
        self.command = command
        # The IDs of the instances on which you want to run the command.\
        # Valid values of N: 1 to 10.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RunCommandResponseBodyTaskId(TeaModel):
    def __init__(
        self,
        task_id: List[str] = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RunCommandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: RunCommandResponseBodyTaskId = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task IDs.
        self.task_id = task_id

    def validate(self):
        if self.task_id:
            self.task_id.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            temp_model = RunCommandResponseBodyTaskId()
            self.task_id = temp_model.from_map(m['TaskId'])
        return self


class RunCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCommandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the ECP instance. Valid values of N: 1 to 20.
        self.key = key
        # The tag value of the ECP instance. Valid values of N: 1 to 20.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class RunInstancesRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        charge_type: str = None,
        client_token: str = None,
        description: str = None,
        eip_bandwidth: int = None,
        image_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        key_pair_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        period_unit: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        resolution: str = None,
        resource_owner_account: str = None,
        security_group_id: str = None,
        tag: List[RunInstancesRequestTag] = None,
        v_switch_id: str = None,
    ):
        # The number of ECS instances that you want to create. Valid values: 1 to 100.
        # 
        # Default value: 1.
        self.amount = amount
        # Specifies whether to enable the auto-payment feature. Default value: true.
        self.auto_pay = auto_pay
        # Specifies whether to enable the auto-renewal feature. This parameter takes effect only if you set InstanceChargeType to PrePaid. Valid values:
        # 
        # *   true
        # *   false (default)
        self.auto_renew = auto_renew
        # The billing method of the ECP instance. Valid values:
        # 
        # *   PrePaid: subscription
        # *   PostPaid (default): pay-as-you-go
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see How to ensure idempotence.
        self.client_token = client_token
        # The description of the ECP instance. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The bandwidth of the elastic IP address (EIP). Valid values: 1 to 200. If you specify this parameter, an ECP instance that uses an EIP with specified bandwidth is automatically created and associated with the ECP instance. If the ECP instance is released, the EIP is also released.
        self.eip_bandwidth = eip_bandwidth
        # The ID of the image.
        self.image_id = image_id
        # The name of the ECP instance. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with `http://` or `https://`. It can contain letters, digits, colons (:), underscores (\_), periods (.), and hyphens (-). The default value of this parameter is the value of the InstanceId parameter.
        self.instance_name = instance_name
        # The specifications of the ECP instance.
        self.instance_type = instance_type
        # The name of the key pair that you want to use to connect to the instance. You can call the ImportKeyPair operation to import a key pair for cloud phones.
        self.key_pair_name = key_pair_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration. Default value: 1.
        # 
        # *   Valid values if you set PeriodUnit to Month: 1, 2, 3, and 6.
        # *   Valid values if you set PeriodUnit to Year: 1, 2, 3, 4, and 5.
        self.period = period
        # The unit of the subscription duration. Valid values:
        # 
        # *   Year
        # *   Month (default)
        self.period_unit = period_unit
        # The private IP address of the cloud phone. When you configure a private IP address for an ECP instance, you must select an idle CIDR block from the CIDR blocks of the vSwitch (VSwitchId). When you specify this parameter, take note of the following items: After you specify the PrivateIpAddress parameter, you must set Amount to 1, which indicates that a cloud phone with a specific private IP address is created.
        self.private_ip_address = private_ip_address
        # The ID of the region.
        self.region_id = region_id
        # The resolution that you want to select for the ECP instance. You can query the resolutions that are supported by the current instance by calling the DescribeInstanceTypes operation and select an appropriate resolution.
        self.resolution = resolution
        self.resource_owner_account = resource_owner_account
        # The ID of the security group that the ECP instance uses. The security group is the same as that of the Elastic Compute Service (ECS) instance that you use.
        self.security_group_id = security_group_id
        # The tags of the ECP instance.
        self.tag = tag
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = RunInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class RunInstancesResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RunInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: RunInstancesResponseBodyInstanceIds = None,
        order_id: str = None,
        request_id: str = None,
        trade_price: float = None,
    ):
        # The IDs of the ECP instances.
        self.instance_ids = instance_ids
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id
        # The price of the ECP resource.
        self.trade_price = trade_price

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            temp_model = RunInstancesResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class RunInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendFileRequest(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        oss_bucket: str = None,
        oss_object: str = None,
        owner_account: str = None,
        owner_id: int = None,
        path: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The IDs of the instances on which you want to run the command. Valid values of N: 1 to 10.
        self.instance_id = instance_id
        # The Object Storage Service (OSS) bucket to which you want to upload the file.
        # 
        # >  Before you import an APK file to the OSS bucket for the first time, add a Resource Access Management (RAM) policy. Otherwise, NoSetRoletoECSServiceAcount appears.
        self.oss_bucket = oss_bucket
        # The name (key) of the file that you want to use as an OSS object.
        self.oss_object = oss_object
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The directory of the file that you want to pull in the cloud phone.
        self.path = path
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_object is not None:
            result['OssObject'] = self.oss_object
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class SendFileResponseBodyTaskId(TeaModel):
    def __init__(
        self,
        task_id: List[str] = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SendFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: SendFileResponseBodyTaskId = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task IDs. Valid values of N: 1 to 100.
        self.task_id = task_id

    def validate(self):
        if self.task_id:
            self.task_id.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            temp_model = SendFileResponseBodyTaskId()
            self.task_id = temp_model.from_map(m['TaskId'])
        return self


class SendFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The instance IDs.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class StartInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstancesRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to forcefully stop the instance. Valid values:
        # 
        # *   true. If you set this parameter to true, cache data that is not written to storage in the instance will be lost after you call this operation, which is similar to the effect of a power-off action.
        # *   false (default)
        self.force = force
        # The instance IDs. Valid values of N: 1 to 100.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class StopInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The resource IDs. You can specify up to 50 resources.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        # The resource type. Valid value:
        # 
        # *   instance: Elastic Cloud Phone (ECP) instance
        self.resource_type = resource_type
        # The tags. You can specify up to 20 tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallApplicationRequest(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        package_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The IDs of the instances on which you want to run the command. Valid values of N: 1 to 10.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the application that you want to uninstall. The name can be up to 1024 bytes in length and can contain only letters, digits, underscores (\_), periods (.), slashes (/), colons (:), and hyphens (-).
        self.package_name = package_name
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UninstallApplicationResponseBodyTaskId(TeaModel):
    def __init__(
        self,
        task_id: List[str] = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UninstallApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: UninstallApplicationResponseBodyTaskId = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.task_id:
            self.task_id.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            temp_model = UninstallApplicationResponseBodyTaskId()
            self.task_id = temp_model.from_map(m['TaskId'])
        return self


class UninstallApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UninstallApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UninstallApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to delete all tags. This parameter takes effect only when the TagKey.N parameter is not specified. Valid values: true and false. Default value: false.
        self.all = all
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The resource IDs. You can specify up to 50 resources.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        # The resource type. Valid value:
        # 
        # *   instance: Elastic Cloud Phone (ECP) instance
        self.resource_type = resource_type
        # The tag keys. You can specify up to 20 tag keys.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageAttributeRequest(TeaModel):
    def __init__(
        self,
        add_account: List[str] = None,
        description: str = None,
        image_id: str = None,
        image_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        remove_account: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The IDs of the Alibaba Cloud accounts that are authorized to share images. You can specify up to 10 Alibaba Cloud accounts.
        self.add_account = add_account
        # The description of the custom image. The description must be 2 to 256 characters in length. It cannot start with `http://` or `https://`. By default, this parameter is empty, which indicates that the original description is retained.
        self.description = description
        # The image ID.
        self.image_id = image_id
        # The name of the custom image. The name must be 2 to 128 characters in length. The name can contain letters, digits, colons (:), underscores (\_), and hyphens (-). It cannot start with `http://` or `https://`. By default, this parameter is empty, which indicates that the original name is retained.
        self.image_name = image_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The IDs of the Alibaba Cloud accounts from which you want to revoke image sharing permissions. You can specify up to 10 Alibaba Cloud accounts.
        self.remove_account = remove_account
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_account is not None:
            result['AddAccount'] = self.add_account
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remove_account is not None:
            result['RemoveAccount'] = self.remove_account
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddAccount') is not None:
            self.add_account = m.get('AddAccount')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemoveAccount') is not None:
            self.remove_account = m.get('RemoveAccount')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateImageAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateImageAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateImageAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateImageAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceAttributeRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance. Valid values of N: 1 to 20.
        self.key = key
        # The tag value of the instance. Valid values of N: 1 to 20.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        instance_name: str = None,
        key_pair_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resolution: str = None,
        resource_owner_account: str = None,
        tag: List[UpdateInstanceAttributeRequestTag] = None,
        vnc_password: str = None,
    ):
        # The instance description. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The instance name. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with `http://` or `https://`. The name can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.instance_name = instance_name
        # The name of the key pair that is used to connect to the instance. To improve the security of an instance, we recommend that you use a key pair to connect to the instance.
        self.key_pair_name = key_pair_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The instance resolution.
        self.resolution = resolution
        self.resource_owner_account = resource_owner_account
        # Details of tags.
        self.tag = tag
        # The VNC password of the instance. The password must be six characters in length and can contain only uppercase letters, lowercase letters, and digits.
        self.vnc_password = vnc_password

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vnc_password is not None:
            result['VncPassword'] = self.vnc_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = UpdateInstanceAttributeRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VncPassword') is not None:
            self.vnc_password = m.get('VncPassword')
        return self


class UpdateInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


