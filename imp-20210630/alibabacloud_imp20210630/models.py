# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class RpcStatus(TeaModel):
    def __init__(
        self,
        code: int = None,
        detail: str = None,
        message: str = None,
    ):
        self.code = code
        self.detail = detail
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
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AssetsAuditAssetResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: RpcStatus = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = RpcStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class CommonAddress(TeaModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        country: str = None,
        state: str = None,
        zip: str = None,
    ):
        self.address = address
        self.city = city
        self.country = country
        self.state = state
        self.zip = zip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.state is not None:
            result['State'] = self.state
        if self.zip is not None:
            result['Zip'] = self.zip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Zip') is not None:
            self.zip = m.get('Zip')
        return self


class CommonMediaResource(TeaModel):
    def __init__(
        self,
        format: str = None,
        id: str = None,
        name: str = None,
        sha_1: str = None,
        size: int = None,
        url: str = None,
    ):
        self.format = format
        self.id = id
        self.name = name
        self.sha_1 = sha_1
        self.size = size
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.sha_1 is not None:
            result['Sha1'] = self.sha_1
        if self.size is not None:
            result['Size'] = self.size
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sha1') is not None:
            self.sha_1 = m.get('Sha1')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class TypeLatLng(TeaModel):
    def __init__(
        self,
        latitude: float = None,
        longitude: float = None,
    ):
        self.latitude = latitude
        self.longitude = longitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        return self


class CommonAsset(TeaModel):
    def __init__(
        self,
        address: CommonAddress = None,
        app_id: str = None,
        audit_status: str = None,
        author: str = None,
        created_at: str = None,
        description: str = None,
        extends: Dict[str, Any] = None,
        id: str = None,
        images: List[CommonMediaResource] = None,
        labels: Dict[str, Any] = None,
        location: TypeLatLng = None,
        source: str = None,
        status: str = None,
        synopsis: str = None,
        tags: List[str] = None,
        title: str = None,
        updated_at: str = None,
        videos: List[CommonMediaResource] = None,
    ):
        self.address = address
        self.app_id = app_id
        self.audit_status = audit_status
        self.author = author
        self.created_at = created_at
        self.description = description
        self.extends = extends
        self.id = id
        self.images = images
        self.labels = labels
        self.location = location
        self.source = source
        self.status = status
        self.synopsis = synopsis
        self.tags = tags
        self.title = title
        self.updated_at = updated_at
        self.videos = videos

    def validate(self):
        if self.address:
            self.address.validate()
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.location:
            self.location.validate()
        if self.videos:
            for k in self.videos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.author is not None:
            result['Author'] = self.author
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.extends is not None:
            result['Extends'] = self.extends
        if self.id is not None:
            result['Id'] = self.id
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.synopsis is not None:
            result['Synopsis'] = self.synopsis
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        result['Videos'] = []
        if self.videos is not None:
            for k in self.videos:
                result['Videos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = CommonAddress()
            self.address = temp_model.from_map(m['Address'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Extends') is not None:
            self.extends = m.get('Extends')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = CommonMediaResource()
                self.images.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Location') is not None:
            temp_model = TypeLatLng()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Synopsis') is not None:
            self.synopsis = m.get('Synopsis')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        self.videos = []
        if m.get('Videos') is not None:
            for k in m.get('Videos'):
                temp_model = CommonMediaResource()
                self.videos.append(temp_model.from_map(k))
        return self


class AssetsCreateAssetResponse(TeaModel):
    def __init__(
        self,
        asset: CommonAsset = None,
        request_id: str = None,
        status: RpcStatus = None,
    ):
        self.asset = asset
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.asset:
            self.asset.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset is not None:
            result['Asset'] = self.asset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asset') is not None:
            temp_model = CommonAsset()
            self.asset = temp_model.from_map(m['Asset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = RpcStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class AssetsDeleteAssetResponse(TeaModel):
    def __init__(
        self,
        asset: CommonAsset = None,
        request_id: str = None,
        status: RpcStatus = None,
    ):
        self.asset = asset
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.asset:
            self.asset.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset is not None:
            result['Asset'] = self.asset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asset') is not None:
            temp_model = CommonAsset()
            self.asset = temp_model.from_map(m['Asset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = RpcStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class AssetsGetAssetResponse(TeaModel):
    def __init__(
        self,
        asset: CommonAsset = None,
        request_id: str = None,
        status: RpcStatus = None,
    ):
        self.asset = asset
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.asset:
            self.asset.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset is not None:
            result['Asset'] = self.asset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asset') is not None:
            temp_model = CommonAsset()
            self.asset = temp_model.from_map(m['Asset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = RpcStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class AssetsListAssetsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        field_mask: str = None,
        max_results: int = None,
        next_token: str = None,
        params: str = None,
        topic: str = None,
    ):
        self.app_id = app_id
        self.field_mask = field_mask
        self.max_results = max_results
        self.next_token = next_token
        self.params = params
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.field_mask is not None:
            result['FieldMask'] = self.field_mask
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.params is not None:
            result['Params'] = self.params
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('FieldMask') is not None:
            self.field_mask = m.get('FieldMask')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class AssetsListAssetsResponse(TeaModel):
    def __init__(
        self,
        assets: List[CommonAsset] = None,
        next_token: str = None,
        request_id: str = None,
        status: RpcStatus = None,
    ):
        self.assets = assets
        self.next_token = next_token
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.assets:
            for k in self.assets:
                if k:
                    k.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Assets'] = []
        if self.assets is not None:
            for k in self.assets:
                result['Assets'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assets = []
        if m.get('Assets') is not None:
            for k in m.get('Assets'):
                temp_model = CommonAsset()
                self.assets.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = RpcStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class AssetsUpdateAssetResponse(TeaModel):
    def __init__(
        self,
        asset: CommonAsset = None,
        request_id: str = None,
        status: RpcStatus = None,
    ):
        self.asset = asset
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.asset:
            self.asset.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset is not None:
            result['Asset'] = self.asset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asset') is not None:
            temp_model = CommonAsset()
            self.asset = temp_model.from_map(m['Asset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = RpcStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class CommonSimpleAsset(TeaModel):
    def __init__(
        self,
        address: CommonAddress = None,
        app_id: str = None,
        audit_status: str = None,
        author: str = None,
        description: str = None,
        extends: Dict[str, Any] = None,
        id: str = None,
        image: CommonMediaResource = None,
        labels: Dict[str, Any] = None,
        location: TypeLatLng = None,
        source: str = None,
        status: str = None,
        synopsis: str = None,
        tags: List[str] = None,
        title: str = None,
        video: CommonMediaResource = None,
    ):
        self.address = address
        self.app_id = app_id
        self.audit_status = audit_status
        self.author = author
        self.description = description
        self.extends = extends
        self.id = id
        self.image = image
        self.labels = labels
        self.location = location
        self.source = source
        self.status = status
        self.synopsis = synopsis
        self.tags = tags
        self.title = title
        self.video = video

    def validate(self):
        if self.address:
            self.address.validate()
        if self.image:
            self.image.validate()
        if self.location:
            self.location.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.author is not None:
            result['Author'] = self.author
        if self.description is not None:
            result['Description'] = self.description
        if self.extends is not None:
            result['Extends'] = self.extends
        if self.id is not None:
            result['Id'] = self.id
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.synopsis is not None:
            result['Synopsis'] = self.synopsis
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.video is not None:
            result['Video'] = self.video.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = CommonAddress()
            self.address = temp_model.from_map(m['Address'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Extends') is not None:
            self.extends = m.get('Extends')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Image') is not None:
            temp_model = CommonMediaResource()
            self.image = temp_model.from_map(m['Image'])
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Location') is not None:
            temp_model = TypeLatLng()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Synopsis') is not None:
            self.synopsis = m.get('Synopsis')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Video') is not None:
            temp_model = CommonMediaResource()
            self.video = temp_model.from_map(m['Video'])
        return self


class BanAllCommentRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.room_id = room_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class BanAllCommentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class BanAllCommentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BanAllCommentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BanAllCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BanCommentRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        ban_comment_time: int = None,
        ban_comment_user: str = None,
        room_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.ban_comment_time = ban_comment_time
        self.ban_comment_user = ban_comment_user
        self.room_id = room_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ban_comment_time is not None:
            result['BanCommentTime'] = self.ban_comment_time
        if self.ban_comment_user is not None:
            result['BanCommentUser'] = self.ban_comment_user
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BanCommentTime') is not None:
            self.ban_comment_time = m.get('BanCommentTime')
        if m.get('BanCommentUser') is not None:
            self.ban_comment_user = m.get('BanCommentUser')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class BanCommentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class BanCommentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BanCommentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BanCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelBanAllCommentRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.room_id = room_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CancelBanAllCommentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CancelBanAllCommentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelBanAllCommentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CancelBanAllCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelBanCommentRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        ban_comment_user: str = None,
        room_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.ban_comment_user = ban_comment_user
        self.room_id = room_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ban_comment_user is not None:
            result['BanCommentUser'] = self.ban_comment_user
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BanCommentUser') is not None:
            self.ban_comment_user = m.get('BanCommentUser')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CancelBanCommentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CancelBanCommentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelBanCommentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CancelBanCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelUserAdminRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.room_id = room_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CancelUserAdminResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class CancelUserAdminResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelUserAdminResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CancelUserAdminResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClassRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_nickname: str = None,
        create_user_id: str = None,
        title: str = None,
    ):
        self.app_id = app_id
        self.create_nickname = create_nickname
        self.create_user_id = create_user_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_nickname is not None:
            result['CreateNickname'] = self.create_nickname
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateNickname') is not None:
            self.create_nickname = m.get('CreateNickname')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateClassResponseBodyResult(TeaModel):
    def __init__(
        self,
        class_id: str = None,
        conf_id: str = None,
        create_nickname: str = None,
        create_user_id: str = None,
        live_id: str = None,
        room_id: str = None,
        status: int = None,
        title: str = None,
        whiteboard_id: str = None,
        whiteboard_record_id: str = None,
    ):
        self.class_id = class_id
        self.conf_id = conf_id
        self.create_nickname = create_nickname
        self.create_user_id = create_user_id
        self.live_id = live_id
        self.room_id = room_id
        self.status = status
        self.title = title
        self.whiteboard_id = whiteboard_id
        self.whiteboard_record_id = whiteboard_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.conf_id is not None:
            result['ConfId'] = self.conf_id
        if self.create_nickname is not None:
            result['CreateNickname'] = self.create_nickname
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.whiteboard_id is not None:
            result['WhiteboardId'] = self.whiteboard_id
        if self.whiteboard_record_id is not None:
            result['WhiteboardRecordId'] = self.whiteboard_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('ConfId') is not None:
            self.conf_id = m.get('ConfId')
        if m.get('CreateNickname') is not None:
            self.create_nickname = m.get('CreateNickname')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('WhiteboardId') is not None:
            self.whiteboard_id = m.get('WhiteboardId')
        if m.get('WhiteboardRecordId') is not None:
            self.whiteboard_record_id = m.get('WhiteboardRecordId')
        return self


class CreateClassResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateClassResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateClassResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClassResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLiveRequest(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        app_id: str = None,
        code_level: int = None,
        introduction: str = None,
        live_id: str = None,
        room_id: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.anchor_id = anchor_id
        self.app_id = app_id
        self.code_level = code_level
        self.introduction = introduction
        self.live_id = live_id
        self.room_id = room_id
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code_level is not None:
            result['CodeLevel'] = self.code_level
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CodeLevel') is not None:
            self.code_level = m.get('CodeLevel')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateLiveResponseBodyResult(TeaModel):
    def __init__(
        self,
        live_id: str = None,
    ):
        self.live_id = live_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class CreateLiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateLiveResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateLiveResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLiveRecordSliceFileRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: int = None,
        file_name: str = None,
        live_id: str = None,
        start_time: int = None,
    ):
        self.app_id = app_id
        self.end_time = end_time
        self.file_name = file_name
        self.live_id = live_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateLiveRecordSliceFileResponseBodyResult(TeaModel):
    def __init__(
        self,
        slice_record_url: str = None,
    ):
        self.slice_record_url = slice_record_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slice_record_url is not None:
            result['SliceRecordUrl'] = self.slice_record_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SliceRecordUrl') is not None:
            self.slice_record_url = m.get('SliceRecordUrl')
        return self


class CreateLiveRecordSliceFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateLiveRecordSliceFileResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateLiveRecordSliceFileResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateLiveRecordSliceFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLiveRecordSliceFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateLiveRecordSliceFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLiveRoomRequest(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        anchor_nick: str = None,
        app_id: str = None,
        cover_url: str = None,
        enable_link_mic: bool = None,
        extension: Dict[str, str] = None,
        notice: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.anchor_id = anchor_id
        self.anchor_nick = anchor_nick
        self.app_id = app_id
        self.cover_url = cover_url
        self.enable_link_mic = enable_link_mic
        self.extension = extension
        self.notice = notice
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.enable_link_mic is not None:
            result['EnableLinkMic'] = self.enable_link_mic
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('EnableLinkMic') is not None:
            self.enable_link_mic = m.get('EnableLinkMic')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateLiveRoomShrinkRequest(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        anchor_nick: str = None,
        app_id: str = None,
        cover_url: str = None,
        enable_link_mic: bool = None,
        extension_shrink: str = None,
        notice: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.anchor_id = anchor_id
        self.anchor_nick = anchor_nick
        self.app_id = app_id
        self.cover_url = cover_url
        self.enable_link_mic = enable_link_mic
        self.extension_shrink = extension_shrink
        self.notice = notice
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.enable_link_mic is not None:
            result['EnableLinkMic'] = self.enable_link_mic
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('EnableLinkMic') is not None:
            self.enable_link_mic = m.get('EnableLinkMic')
        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateLiveRoomResponseBodyResultArtcInfo(TeaModel):
    def __init__(
        self,
        artc_h5url: str = None,
        artc_url: str = None,
    ):
        self.artc_h5url = artc_h5url
        self.artc_url = artc_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artc_h5url is not None:
            result['ArtcH5Url'] = self.artc_h5url
        if self.artc_url is not None:
            result['ArtcUrl'] = self.artc_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtcH5Url') is not None:
            self.artc_h5url = m.get('ArtcH5Url')
        if m.get('ArtcUrl') is not None:
            self.artc_url = m.get('ArtcUrl')
        return self


class CreateLiveRoomResponseBodyResultPluginInstanceInfoList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        extension: Dict[str, str] = None,
        plugin_id: str = None,
        plugin_type: str = None,
    ):
        self.create_time = create_time
        self.extension = extension
        self.plugin_id = plugin_id
        self.plugin_type = plugin_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        return self


class CreateLiveRoomResponseBodyResult(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        anchor_nick: str = None,
        app_id: str = None,
        artc_info: CreateLiveRoomResponseBodyResultArtcInfo = None,
        chat_id: str = None,
        cover_url: str = None,
        extension: Dict[str, str] = None,
        hls_url: str = None,
        live_id: str = None,
        live_url: str = None,
        notice: str = None,
        playback_url: str = None,
        plugin_instance_info_list: List[CreateLiveRoomResponseBodyResultPluginInstanceInfoList] = None,
        push_url: str = None,
        room_id: str = None,
        title: str = None,
    ):
        self.anchor_id = anchor_id
        self.anchor_nick = anchor_nick
        self.app_id = app_id
        self.artc_info = artc_info
        self.chat_id = chat_id
        self.cover_url = cover_url
        self.extension = extension
        self.hls_url = hls_url
        self.live_id = live_id
        self.live_url = live_url
        self.notice = notice
        self.playback_url = playback_url
        self.plugin_instance_info_list = plugin_instance_info_list
        self.push_url = push_url
        self.room_id = room_id
        self.title = title

    def validate(self):
        if self.artc_info:
            self.artc_info.validate()
        if self.plugin_instance_info_list:
            for k in self.plugin_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.artc_info is not None:
            result['ArtcInfo'] = self.artc_info.to_map()
        if self.chat_id is not None:
            result['ChatId'] = self.chat_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.hls_url is not None:
            result['HlsUrl'] = self.hls_url
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.playback_url is not None:
            result['PlaybackUrl'] = self.playback_url
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArtcInfo') is not None:
            temp_model = CreateLiveRoomResponseBodyResultArtcInfo()
            self.artc_info = temp_model.from_map(m['ArtcInfo'])
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('HlsUrl') is not None:
            self.hls_url = m.get('HlsUrl')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('PlaybackUrl') is not None:
            self.playback_url = m.get('PlaybackUrl')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = CreateLiveRoomResponseBodyResultPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateLiveRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateLiveRoomResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateLiveRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateLiveRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLiveRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateLiveRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        extension: Dict[str, str] = None,
        notice: str = None,
        room_id: str = None,
        room_owner_id: str = None,
        template_id: str = None,
        title: str = None,
    ):
        self.app_id = app_id
        self.extension = extension
        self.notice = notice
        self.room_id = room_id
        self.room_owner_id = room_owner_id
        self.template_id = template_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateRoomShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        extension_shrink: str = None,
        notice: str = None,
        room_id: str = None,
        room_owner_id: str = None,
        template_id: str = None,
        title: str = None,
    ):
        self.app_id = app_id
        self.extension_shrink = extension_shrink
        self.notice = notice
        self.room_id = room_id
        self.room_owner_id = room_owner_id
        self.template_id = template_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateRoomResponseBodyResult(TeaModel):
    def __init__(
        self,
        room_id: str = None,
    ):
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class CreateRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateRoomResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSensitiveWordRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        word_list: List[str] = None,
    ):
        self.app_id = app_id
        self.word_list = word_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.word_list is not None:
            result['WordList'] = self.word_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WordList') is not None:
            self.word_list = m.get('WordList')
        return self


class CreateSensitiveWordShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        word_list_shrink: str = None,
    ):
        self.app_id = app_id
        self.word_list_shrink = word_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.word_list_shrink is not None:
            result['WordList'] = self.word_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WordList') is not None:
            self.word_list_shrink = m.get('WordList')
        return self


class CreateSensitiveWordResponseBodyResult(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSensitiveWordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateSensitiveWordResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateSensitiveWordResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateSensitiveWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSensitiveWordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateSensitiveWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClassRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        class_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.class_id = class_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteClassResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClassResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCommentRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        comment_id_list: List[str] = None,
        room_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.comment_id_list = comment_id_list
        self.room_id = room_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.comment_id_list is not None:
            result['CommentIdList'] = self.comment_id_list
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommentIdList') is not None:
            self.comment_id_list = m.get('CommentIdList')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteCommentResponseBodyResult(TeaModel):
    def __init__(
        self,
        delete_result: bool = None,
    ):
        self.delete_result = delete_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_result is not None:
            result['DeleteResult'] = self.delete_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteResult') is not None:
            self.delete_result = m.get('DeleteResult')
        return self


class DeleteCommentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DeleteCommentResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteCommentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteCommentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCommentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCommentByCreatorIdRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        comment_id_list: List[str] = None,
        creator_id: str = None,
        room_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.comment_id_list = comment_id_list
        self.creator_id = creator_id
        self.room_id = room_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.comment_id_list is not None:
            result['CommentIdList'] = self.comment_id_list
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommentIdList') is not None:
            self.comment_id_list = m.get('CommentIdList')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteCommentByCreatorIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        delete_result: bool = None,
    ):
        self.delete_result = delete_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_result is not None:
            result['DeleteResult'] = self.delete_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteResult') is not None:
            self.delete_result = m.get('DeleteResult')
        return self


class DeleteCommentByCreatorIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DeleteCommentByCreatorIdResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteCommentByCreatorIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteCommentByCreatorIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCommentByCreatorIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteCommentByCreatorIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConferenceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        conference_id: str = None,
        room_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.conference_id = conference_id
        self.room_id = room_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteConferenceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteConferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConferenceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLiveRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
    ):
        self.live_id = live_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class DeleteLiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLiveFilesByIdRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id: str = None,
    ):
        self.app_id = app_id
        self.live_id = live_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class DeleteLiveFilesByIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteLiveFilesByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLiveFilesByIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteLiveFilesByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLiveRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.live_id = live_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteLiveRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteLiveRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLiveRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteLiveRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
    ):
        self.app_id = app_id
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class DeleteRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSensitiveWordRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        word_list: List[str] = None,
    ):
        self.app_id = app_id
        self.word_list = word_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.word_list is not None:
            result['WordList'] = self.word_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WordList') is not None:
            self.word_list = m.get('WordList')
        return self


class DeleteSensitiveWordShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        word_list_shrink: str = None,
    ):
        self.app_id = app_id
        self.word_list_shrink = word_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.word_list_shrink is not None:
            result['WordList'] = self.word_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WordList') is not None:
            self.word_list_shrink = m.get('WordList')
        return self


class DeleteSensitiveWordResponseBodyResult(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSensitiveWordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DeleteSensitiveWordResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteSensitiveWordResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteSensitiveWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSensitiveWordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteSensitiveWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterImpPlayBackTimeByLiveIdRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        live_id: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.live_id = live_id
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterImpPlayBackTimeByLiveIdResponseBodyData(TeaModel):
    def __init__(
        self,
        watch_time: int = None,
    ):
        self.watch_time = watch_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watch_time is not None:
            result['WatchTime'] = self.watch_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatchTime') is not None:
            self.watch_time = m.get('WatchTime')
        return self


class DescribeMeterImpPlayBackTimeByLiveIdResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterImpPlayBackTimeByLiveIdResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeMeterImpPlayBackTimeByLiveIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterImpPlayBackTimeByLiveIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMeterImpPlayBackTimeByLiveIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeMeterImpPlayBackTimeByLiveIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterImpWatchLiveTimeByLiveIdRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id: str = None,
    ):
        self.app_id = app_id
        self.live_id = live_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class DescribeMeterImpWatchLiveTimeByLiveIdResponseBodyData(TeaModel):
    def __init__(
        self,
        watch_time_in_latency: int = None,
        watch_time_in_low_latency: int = None,
    ):
        self.watch_time_in_latency = watch_time_in_latency
        self.watch_time_in_low_latency = watch_time_in_low_latency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watch_time_in_latency is not None:
            result['WatchTimeInLatency'] = self.watch_time_in_latency
        if self.watch_time_in_low_latency is not None:
            result['WatchTimeInLowLatency'] = self.watch_time_in_low_latency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatchTimeInLatency') is not None:
            self.watch_time_in_latency = m.get('WatchTimeInLatency')
        if m.get('WatchTimeInLowLatency') is not None:
            self.watch_time_in_low_latency = m.get('WatchTimeInLowLatency')
        return self


class DescribeMeterImpWatchLiveTimeByLiveIdResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterImpWatchLiveTimeByLiveIdResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeMeterImpWatchLiveTimeByLiveIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterImpWatchLiveTimeByLiveIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMeterImpWatchLiveTimeByLiveIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeMeterImpWatchLiveTimeByLiveIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthTokenRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_key: str = None,
        device_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.app_key = app_key
        self.device_id = device_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetAuthTokenResponseBodyResult(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        access_token_expired_time: int = None,
        refresh_token: str = None,
    ):
        self.access_token = access_token
        self.access_token_expired_time = access_token_expired_time
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class GetAuthTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetAuthTokenResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetAuthTokenResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAuthTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAuthTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClassDetailRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        class_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.class_id = class_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetClassDetailResponseBodyResult(TeaModel):
    def __init__(
        self,
        class_id: str = None,
        conf_id: str = None,
        create_nickname: str = None,
        create_user_id: str = None,
        end_time: int = None,
        live_id: str = None,
        room_id: str = None,
        start_time: int = None,
        status: int = None,
        title: str = None,
        whiteboard_id: str = None,
        whiteboard_record_id: str = None,
    ):
        self.class_id = class_id
        self.conf_id = conf_id
        self.create_nickname = create_nickname
        self.create_user_id = create_user_id
        self.end_time = end_time
        self.live_id = live_id
        self.room_id = room_id
        self.start_time = start_time
        self.status = status
        self.title = title
        self.whiteboard_id = whiteboard_id
        self.whiteboard_record_id = whiteboard_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.conf_id is not None:
            result['ConfId'] = self.conf_id
        if self.create_nickname is not None:
            result['CreateNickname'] = self.create_nickname
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.whiteboard_id is not None:
            result['WhiteboardId'] = self.whiteboard_id
        if self.whiteboard_record_id is not None:
            result['WhiteboardRecordId'] = self.whiteboard_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('ConfId') is not None:
            self.conf_id = m.get('ConfId')
        if m.get('CreateNickname') is not None:
            self.create_nickname = m.get('CreateNickname')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('WhiteboardId') is not None:
            self.whiteboard_id = m.get('WhiteboardId')
        if m.get('WhiteboardRecordId') is not None:
            self.whiteboard_record_id = m.get('WhiteboardRecordId')
        return self


class GetClassDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetClassDetailResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetClassDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetClassDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClassDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetClassDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClassRecordRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        class_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.class_id = class_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetClassRecordResponseBodyResult(TeaModel):
    def __init__(
        self,
        playback_url_map: Dict[str, List[str]] = None,
    ):
        self.playback_url_map = playback_url_map

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playback_url_map is not None:
            result['PlaybackUrlMap'] = self.playback_url_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybackUrlMap') is not None:
            self.playback_url_map = m.get('PlaybackUrlMap')
        return self


class GetClassRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetClassRecordResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetClassRecordResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetClassRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClassRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetClassRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConferenceRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
    ):
        self.conference_id = conference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        return self


class GetConferenceResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        conference_id: str = None,
        create_time: int = None,
        playback_url: str = None,
        room_id: str = None,
        status: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.conference_id = conference_id
        self.create_time = create_time
        self.playback_url = playback_url
        self.room_id = room_id
        self.status = status
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.playback_url is not None:
            result['PlaybackUrl'] = self.playback_url
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PlaybackUrl') is not None:
            self.playback_url = m.get('PlaybackUrl')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetConferenceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetConferenceResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetConferenceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetConferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConferenceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
    ):
        self.live_id = live_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class GetLiveResponseBodyResultArtcInfo(TeaModel):
    def __init__(
        self,
        artc_h5url: str = None,
        artc_url: str = None,
    ):
        self.artc_h5url = artc_h5url
        self.artc_url = artc_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artc_h5url is not None:
            result['ArtcH5Url'] = self.artc_h5url
        if self.artc_url is not None:
            result['ArtcUrl'] = self.artc_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtcH5Url') is not None:
            self.artc_h5url = m.get('ArtcH5Url')
        if m.get('ArtcUrl') is not None:
            self.artc_url = m.get('ArtcUrl')
        return self


class GetLiveResponseBodyResultPlayUrlInfoList(TeaModel):
    def __init__(
        self,
        code_level: int = None,
        flv_url: str = None,
        hls_url: str = None,
        rtmp_url: str = None,
    ):
        self.code_level = code_level
        self.flv_url = flv_url
        self.hls_url = hls_url
        self.rtmp_url = rtmp_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_level is not None:
            result['CodeLevel'] = self.code_level
        if self.flv_url is not None:
            result['FlvUrl'] = self.flv_url
        if self.hls_url is not None:
            result['HlsUrl'] = self.hls_url
        if self.rtmp_url is not None:
            result['RtmpUrl'] = self.rtmp_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeLevel') is not None:
            self.code_level = m.get('CodeLevel')
        if m.get('FlvUrl') is not None:
            self.flv_url = m.get('FlvUrl')
        if m.get('HlsUrl') is not None:
            self.hls_url = m.get('HlsUrl')
        if m.get('RtmpUrl') is not None:
            self.rtmp_url = m.get('RtmpUrl')
        return self


class GetLiveResponseBodyResult(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        app_id: str = None,
        artc_info: GetLiveResponseBodyResultArtcInfo = None,
        code_level: int = None,
        cover_url: str = None,
        create_time: int = None,
        duration: int = None,
        end_time: int = None,
        hls_url: str = None,
        introduction: str = None,
        live_id: str = None,
        live_url: str = None,
        play_url_info_list: List[GetLiveResponseBodyResultPlayUrlInfoList] = None,
        playback_url: str = None,
        push_url: str = None,
        room_id: str = None,
        status: str = None,
        title: str = None,
        user_define_field: str = None,
        user_id: str = None,
    ):
        self.anchor_id = anchor_id
        self.app_id = app_id
        self.artc_info = artc_info
        self.code_level = code_level
        self.cover_url = cover_url
        self.create_time = create_time
        self.duration = duration
        self.end_time = end_time
        self.hls_url = hls_url
        self.introduction = introduction
        self.live_id = live_id
        self.live_url = live_url
        self.play_url_info_list = play_url_info_list
        self.playback_url = playback_url
        self.push_url = push_url
        self.room_id = room_id
        self.status = status
        self.title = title
        self.user_define_field = user_define_field
        self.user_id = user_id

    def validate(self):
        if self.artc_info:
            self.artc_info.validate()
        if self.play_url_info_list:
            for k in self.play_url_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.artc_info is not None:
            result['ArtcInfo'] = self.artc_info.to_map()
        if self.code_level is not None:
            result['CodeLevel'] = self.code_level
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hls_url is not None:
            result['HlsUrl'] = self.hls_url
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        result['PlayUrlInfoList'] = []
        if self.play_url_info_list is not None:
            for k in self.play_url_info_list:
                result['PlayUrlInfoList'].append(k.to_map() if k else None)
        if self.playback_url is not None:
            result['PlaybackUrl'] = self.playback_url
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.user_define_field is not None:
            result['UserDefineField'] = self.user_define_field
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArtcInfo') is not None:
            temp_model = GetLiveResponseBodyResultArtcInfo()
            self.artc_info = temp_model.from_map(m['ArtcInfo'])
        if m.get('CodeLevel') is not None:
            self.code_level = m.get('CodeLevel')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HlsUrl') is not None:
            self.hls_url = m.get('HlsUrl')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        self.play_url_info_list = []
        if m.get('PlayUrlInfoList') is not None:
            for k in m.get('PlayUrlInfoList'):
                temp_model = GetLiveResponseBodyResultPlayUrlInfoList()
                self.play_url_info_list.append(temp_model.from_map(k))
        if m.get('PlaybackUrl') is not None:
            self.playback_url = m.get('PlaybackUrl')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserDefineField') is not None:
            self.user_define_field = m.get('UserDefineField')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetLiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetLiveResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetLiveResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveRecordRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.live_id = live_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetLiveRecordResponseBodyResult(TeaModel):
    def __init__(
        self,
        playback_url_map: Dict[str, List[str]] = None,
    ):
        self.playback_url_map = playback_url_map

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playback_url_map is not None:
            result['PlaybackUrlMap'] = self.playback_url_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybackUrlMap') is not None:
            self.playback_url_map = m.get('PlaybackUrlMap')
        return self


class GetLiveRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetLiveRecordResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetLiveRecordResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLiveRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetLiveRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id: str = None,
    ):
        self.app_id = app_id
        self.live_id = live_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class GetLiveRoomResponseBodyResultArtcInfo(TeaModel):
    def __init__(
        self,
        artc_h5url: str = None,
        artc_url: str = None,
    ):
        self.artc_h5url = artc_h5url
        self.artc_url = artc_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artc_h5url is not None:
            result['ArtcH5Url'] = self.artc_h5url
        if self.artc_url is not None:
            result['ArtcUrl'] = self.artc_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtcH5Url') is not None:
            self.artc_h5url = m.get('ArtcH5Url')
        if m.get('ArtcUrl') is not None:
            self.artc_url = m.get('ArtcUrl')
        return self


class GetLiveRoomResponseBodyResultPluginInstanceInfoList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        extension: Dict[str, str] = None,
        plugin_id: str = None,
        plugin_type: str = None,
    ):
        self.create_time = create_time
        self.extension = extension
        self.plugin_id = plugin_id
        self.plugin_type = plugin_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        return self


class GetLiveRoomResponseBodyResult(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        anchor_nick: str = None,
        app_id: str = None,
        artc_info: GetLiveRoomResponseBodyResultArtcInfo = None,
        chat_id: str = None,
        conf_id: str = None,
        cover_url: str = None,
        create_time: int = None,
        enable_link_mic: bool = None,
        end_time: int = None,
        extension: Dict[str, str] = None,
        hls_url: str = None,
        hls_url_https: str = None,
        live_id: str = None,
        live_url: str = None,
        live_url_https: str = None,
        notice: str = None,
        online_count: int = None,
        playback_url: str = None,
        playback_url_https: str = None,
        plugin_instance_info_list: List[GetLiveRoomResponseBodyResultPluginInstanceInfoList] = None,
        push_url: str = None,
        pv: int = None,
        room_id: str = None,
        rtmp_url: str = None,
        start_time: int = None,
        status: int = None,
        title: str = None,
        uv: int = None,
    ):
        self.anchor_id = anchor_id
        self.anchor_nick = anchor_nick
        self.app_id = app_id
        self.artc_info = artc_info
        self.chat_id = chat_id
        self.conf_id = conf_id
        self.cover_url = cover_url
        self.create_time = create_time
        self.enable_link_mic = enable_link_mic
        self.end_time = end_time
        self.extension = extension
        self.hls_url = hls_url
        self.hls_url_https = hls_url_https
        self.live_id = live_id
        self.live_url = live_url
        self.live_url_https = live_url_https
        self.notice = notice
        self.online_count = online_count
        self.playback_url = playback_url
        self.playback_url_https = playback_url_https
        self.plugin_instance_info_list = plugin_instance_info_list
        self.push_url = push_url
        self.pv = pv
        self.room_id = room_id
        self.rtmp_url = rtmp_url
        self.start_time = start_time
        self.status = status
        self.title = title
        self.uv = uv

    def validate(self):
        if self.artc_info:
            self.artc_info.validate()
        if self.plugin_instance_info_list:
            for k in self.plugin_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.artc_info is not None:
            result['ArtcInfo'] = self.artc_info.to_map()
        if self.chat_id is not None:
            result['ChatId'] = self.chat_id
        if self.conf_id is not None:
            result['ConfId'] = self.conf_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_link_mic is not None:
            result['EnableLinkMic'] = self.enable_link_mic
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.hls_url is not None:
            result['HlsUrl'] = self.hls_url
        if self.hls_url_https is not None:
            result['HlsUrlHttps'] = self.hls_url_https
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        if self.live_url_https is not None:
            result['LiveUrlHttps'] = self.live_url_https
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        if self.playback_url is not None:
            result['PlaybackUrl'] = self.playback_url
        if self.playback_url_https is not None:
            result['PlaybackUrlHttps'] = self.playback_url_https
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.pv is not None:
            result['Pv'] = self.pv
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.rtmp_url is not None:
            result['RtmpUrl'] = self.rtmp_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['Uv'] = self.uv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArtcInfo') is not None:
            temp_model = GetLiveRoomResponseBodyResultArtcInfo()
            self.artc_info = temp_model.from_map(m['ArtcInfo'])
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')
        if m.get('ConfId') is not None:
            self.conf_id = m.get('ConfId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableLinkMic') is not None:
            self.enable_link_mic = m.get('EnableLinkMic')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('HlsUrl') is not None:
            self.hls_url = m.get('HlsUrl')
        if m.get('HlsUrlHttps') is not None:
            self.hls_url_https = m.get('HlsUrlHttps')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        if m.get('LiveUrlHttps') is not None:
            self.live_url_https = m.get('LiveUrlHttps')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        if m.get('PlaybackUrl') is not None:
            self.playback_url = m.get('PlaybackUrl')
        if m.get('PlaybackUrlHttps') is not None:
            self.playback_url_https = m.get('PlaybackUrlHttps')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = GetLiveRoomResponseBodyResultPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('Pv') is not None:
            self.pv = m.get('Pv')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RtmpUrl') is not None:
            self.rtmp_url = m.get('RtmpUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        return self


class GetLiveRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetLiveRoomResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetLiveRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLiveRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetLiveRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveRoomStatisticsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id: str = None,
    ):
        self.app_id = app_id
        self.live_id = live_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class GetLiveRoomStatisticsResponseBodyResult(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        like_count: int = None,
        live_id: str = None,
        message_count: int = None,
        online_count: int = None,
        pv: int = None,
        start_time: int = None,
        status: int = None,
        uv: int = None,
        watch_live_time: int = None,
    ):
        self.end_time = end_time
        self.like_count = like_count
        self.live_id = live_id
        self.message_count = message_count
        self.online_count = online_count
        self.pv = pv
        self.start_time = start_time
        self.status = status
        self.uv = uv
        self.watch_live_time = watch_live_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.like_count is not None:
            result['LikeCount'] = self.like_count
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.message_count is not None:
            result['MessageCount'] = self.message_count
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        if self.pv is not None:
            result['Pv'] = self.pv
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.uv is not None:
            result['Uv'] = self.uv
        if self.watch_live_time is not None:
            result['WatchLiveTime'] = self.watch_live_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LikeCount') is not None:
            self.like_count = m.get('LikeCount')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('MessageCount') is not None:
            self.message_count = m.get('MessageCount')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        if m.get('Pv') is not None:
            self.pv = m.get('Pv')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        if m.get('WatchLiveTime') is not None:
            self.watch_live_time = m.get('WatchLiveTime')
        return self


class GetLiveRoomStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetLiveRoomStatisticsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetLiveRoomStatisticsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveRoomStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLiveRoomStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetLiveRoomStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveRoomUserStatisticsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.app_id = app_id
        self.live_id = live_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetLiveRoomUserStatisticsResponseBodyResultUserStatisticsList(TeaModel):
    def __init__(
        self,
        comment_count: int = None,
        like_count: int = None,
        user_id: str = None,
        watch_live_time: int = None,
    ):
        self.comment_count = comment_count
        self.like_count = like_count
        self.user_id = user_id
        self.watch_live_time = watch_live_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment_count is not None:
            result['CommentCount'] = self.comment_count
        if self.like_count is not None:
            result['LikeCount'] = self.like_count
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.watch_live_time is not None:
            result['WatchLiveTime'] = self.watch_live_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommentCount') is not None:
            self.comment_count = m.get('CommentCount')
        if m.get('LikeCount') is not None:
            self.like_count = m.get('LikeCount')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WatchLiveTime') is not None:
            self.watch_live_time = m.get('WatchLiveTime')
        return self


class GetLiveRoomUserStatisticsResponseBodyResult(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        live_id: str = None,
        page_total: int = None,
        total_count: int = None,
        user_statistics_list: List[GetLiveRoomUserStatisticsResponseBodyResultUserStatisticsList] = None,
    ):
        self.has_more = has_more
        self.live_id = live_id
        self.page_total = page_total
        self.total_count = total_count
        self.user_statistics_list = user_statistics_list

    def validate(self):
        if self.user_statistics_list:
            for k in self.user_statistics_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UserStatisticsList'] = []
        if self.user_statistics_list is not None:
            for k in self.user_statistics_list:
                result['UserStatisticsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.user_statistics_list = []
        if m.get('UserStatisticsList') is not None:
            for k in m.get('UserStatisticsList'):
                temp_model = GetLiveRoomUserStatisticsResponseBodyResultUserStatisticsList()
                self.user_statistics_list.append(temp_model.from_map(k))
        return self


class GetLiveRoomUserStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetLiveRoomUserStatisticsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetLiveRoomUserStatisticsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveRoomUserStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLiveRoomUserStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetLiveRoomUserStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
    ):
        self.app_id = app_id
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        extension: Dict[str, str] = None,
        plugin_id: str = None,
        plugin_type: str = None,
    ):
        self.create_time = create_time
        self.extension = extension
        self.plugin_id = plugin_id
        self.plugin_type = plugin_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        return self


class GetRoomResponseBodyResultRoomInfo(TeaModel):
    def __init__(
        self,
        admin_id_list: List[str] = None,
        app_id: str = None,
        create_time: int = None,
        extension: Dict[str, str] = None,
        notice: str = None,
        online_count: int = None,
        plugin_instance_info_list: List[GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList] = None,
        pv: int = None,
        room_id: str = None,
        room_owner_id: str = None,
        template_id: str = None,
        title: str = None,
        uv: int = None,
    ):
        self.admin_id_list = admin_id_list
        self.app_id = app_id
        self.create_time = create_time
        self.extension = extension
        self.notice = notice
        self.online_count = online_count
        self.plugin_instance_info_list = plugin_instance_info_list
        self.pv = pv
        self.room_id = room_id
        self.room_owner_id = room_owner_id
        self.template_id = template_id
        self.title = title
        self.uv = uv

    def validate(self):
        if self.plugin_instance_info_list:
            for k in self.plugin_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_id_list is not None:
            result['AdminIdList'] = self.admin_id_list
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        if self.pv is not None:
            result['Pv'] = self.pv
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['Uv'] = self.uv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminIdList') is not None:
            self.admin_id_list = m.get('AdminIdList')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        if m.get('Pv') is not None:
            self.pv = m.get('Pv')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        return self


class GetRoomResponseBodyResult(TeaModel):
    def __init__(
        self,
        room_info: GetRoomResponseBodyResultRoomInfo = None,
    ):
        self.room_info = room_info

    def validate(self):
        if self.room_info:
            self.room_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_info is not None:
            result['RoomInfo'] = self.room_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomInfo') is not None:
            temp_model = GetRoomResponseBodyResultRoomInfo()
            self.room_info = temp_model.from_map(m['RoomInfo'])
        return self


class GetRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetRoomResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStandardRoomJumpUrlRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_key: str = None,
        biz_id: str = None,
        biz_type: str = None,
        platform: str = None,
        user_id: str = None,
        user_nick: str = None,
    ):
        self.app_id = app_id
        self.app_key = app_key
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.platform = platform
        self.user_id = user_id
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        return self


class GetStandardRoomJumpUrlResponseBodyResult(TeaModel):
    def __init__(
        self,
        standard_room_jump_url: str = None,
    ):
        self.standard_room_jump_url = standard_room_jump_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.standard_room_jump_url is not None:
            result['StandardRoomJumpUrl'] = self.standard_room_jump_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardRoomJumpUrl') is not None:
            self.standard_room_jump_url = m.get('StandardRoomJumpUrl')
        return self


class GetStandardRoomJumpUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetStandardRoomJumpUrlResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetStandardRoomJumpUrlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetStandardRoomJumpUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStandardRoomJumpUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetStandardRoomJumpUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KickRoomUserRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        block_time: int = None,
        kick_user: str = None,
        room_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.block_time = block_time
        self.kick_user = kick_user
        self.room_id = room_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.block_time is not None:
            result['BlockTime'] = self.block_time
        if self.kick_user is not None:
            result['KickUser'] = self.kick_user
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BlockTime') is not None:
            self.block_time = m.get('BlockTime')
        if m.get('KickUser') is not None:
            self.kick_user = m.get('KickUser')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class KickRoomUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class KickRoomUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KickRoomUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = KickRoomUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClassesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
    ):
        self.app_id = app_id
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListClassesResponseBodyResultClassList(TeaModel):
    def __init__(
        self,
        class_id: str = None,
        conf_id: str = None,
        create_nickname: str = None,
        create_user_id: str = None,
        end_time: int = None,
        live_id: str = None,
        room_id: str = None,
        start_time: int = None,
        status: int = None,
        title: str = None,
        whiteboard_id: str = None,
        whiteboard_record_id: str = None,
    ):
        self.class_id = class_id
        self.conf_id = conf_id
        self.create_nickname = create_nickname
        self.create_user_id = create_user_id
        self.end_time = end_time
        self.live_id = live_id
        self.room_id = room_id
        self.start_time = start_time
        self.status = status
        self.title = title
        self.whiteboard_id = whiteboard_id
        self.whiteboard_record_id = whiteboard_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.conf_id is not None:
            result['ConfId'] = self.conf_id
        if self.create_nickname is not None:
            result['CreateNickname'] = self.create_nickname
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.whiteboard_id is not None:
            result['WhiteboardId'] = self.whiteboard_id
        if self.whiteboard_record_id is not None:
            result['WhiteboardRecordId'] = self.whiteboard_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('ConfId') is not None:
            self.conf_id = m.get('ConfId')
        if m.get('CreateNickname') is not None:
            self.create_nickname = m.get('CreateNickname')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('WhiteboardId') is not None:
            self.whiteboard_id = m.get('WhiteboardId')
        if m.get('WhiteboardRecordId') is not None:
            self.whiteboard_record_id = m.get('WhiteboardRecordId')
        return self


class ListClassesResponseBodyResult(TeaModel):
    def __init__(
        self,
        class_list: List[ListClassesResponseBodyResultClassList] = None,
        has_more: bool = None,
        page_total: int = None,
        total_count: int = None,
    ):
        self.class_list = class_list
        self.has_more = has_more
        self.page_total = page_total
        self.total_count = total_count

    def validate(self):
        if self.class_list:
            for k in self.class_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClassList'] = []
        if self.class_list is not None:
            for k in self.class_list:
                result['ClassList'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.class_list = []
        if m.get('ClassList') is not None:
            for k in m.get('ClassList'):
                temp_model = ListClassesResponseBodyResultClassList()
                self.class_list.append(temp_model.from_map(k))
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClassesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListClassesResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListClassesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListClassesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClassesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListClassesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommentsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        creator_id: str = None,
        page_num: int = None,
        page_size: int = None,
        room_id: str = None,
        sort_type: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.creator_id = creator_id
        self.page_num = page_num
        self.page_size = page_size
        self.room_id = room_id
        self.sort_type = sort_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListCommentsResponseBodyResultCommentVOList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        comment_id: str = None,
        content: str = None,
        create_at: int = None,
        extension: Dict[str, str] = None,
        room_id: str = None,
        sender_id: str = None,
        sender_nick: str = None,
    ):
        self.app_id = app_id
        self.comment_id = comment_id
        self.content = content
        self.create_at = create_at
        self.extension = extension
        self.room_id = room_id
        self.sender_id = sender_id
        self.sender_nick = sender_nick

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.comment_id is not None:
            result['CommentId'] = self.comment_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_at is not None:
            result['CreateAt'] = self.create_at
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommentId') is not None:
            self.comment_id = m.get('CommentId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateAt') is not None:
            self.create_at = m.get('CreateAt')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        return self


class ListCommentsResponseBodyResult(TeaModel):
    def __init__(
        self,
        comment_volist: List[ListCommentsResponseBodyResultCommentVOList] = None,
        has_more: bool = None,
        page_total: int = None,
        total_count: int = None,
    ):
        self.comment_volist = comment_volist
        self.has_more = has_more
        self.page_total = page_total
        self.total_count = total_count

    def validate(self):
        if self.comment_volist:
            for k in self.comment_volist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommentVOList'] = []
        if self.comment_volist is not None:
            for k in self.comment_volist:
                result['CommentVOList'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.comment_volist = []
        if m.get('CommentVOList') is not None:
            for k in m.get('CommentVOList'):
                temp_model = ListCommentsResponseBodyResultCommentVOList()
                self.comment_volist.append(temp_model.from_map(k))
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCommentsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListCommentsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListCommentsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListCommentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCommentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListCommentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConferenceUsersRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.conference_id = conference_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListConferenceUsersResponseBodyResultConferenceUserList(TeaModel):
    def __init__(
        self,
        status: str = None,
        user_id: str = None,
    ):
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListConferenceUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        conference_user_list: List[ListConferenceUsersResponseBodyResultConferenceUserList] = None,
        has_more: bool = None,
        page_total: int = None,
        total_count: int = None,
    ):
        self.conference_user_list = conference_user_list
        self.has_more = has_more
        self.page_total = page_total
        self.total_count = total_count

    def validate(self):
        if self.conference_user_list:
            for k in self.conference_user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConferenceUserList'] = []
        if self.conference_user_list is not None:
            for k in self.conference_user_list:
                result['ConferenceUserList'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conference_user_list = []
        if m.get('ConferenceUserList') is not None:
            for k in m.get('ConferenceUserList'):
                temp_model = ListConferenceUsersResponseBodyResultConferenceUserList()
                self.conference_user_list.append(temp_model.from_map(k))
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListConferenceUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListConferenceUsersResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListConferenceUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListConferenceUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConferenceUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListConferenceUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLiveFilesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id: str = None,
    ):
        self.app_id = app_id
        self.live_id = live_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class ListLiveFilesResponseBodyResultFileList(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        url: str = None,
    ):
        self.file_name = file_name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListLiveFilesResponseBodyResult(TeaModel):
    def __init__(
        self,
        file_list: List[ListLiveFilesResponseBodyResultFileList] = None,
    ):
        self.file_list = file_list

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = ListLiveFilesResponseBodyResultFileList()
                self.file_list.append(temp_model.from_map(k))
        return self


class ListLiveFilesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListLiveFilesResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListLiveFilesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListLiveFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLiveFilesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListLiveFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLiveRoomsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
    ):
        self.app_id = app_id
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLiveRoomsResponseBodyResultLiveList(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        anchor_nick: str = None,
        app_id: str = None,
        chat_id: str = None,
        cover_url: str = None,
        create_time: int = None,
        end_time: int = None,
        extension: Dict[str, str] = None,
        live_id: str = None,
        notice: str = None,
        online_count: int = None,
        pv: int = None,
        room_id: str = None,
        start_time: int = None,
        status: int = None,
        title: str = None,
        uv: int = None,
    ):
        self.anchor_id = anchor_id
        self.anchor_nick = anchor_nick
        self.app_id = app_id
        self.chat_id = chat_id
        self.cover_url = cover_url
        self.create_time = create_time
        self.end_time = end_time
        self.extension = extension
        self.live_id = live_id
        self.notice = notice
        self.online_count = online_count
        self.pv = pv
        self.room_id = room_id
        self.start_time = start_time
        self.status = status
        self.title = title
        self.uv = uv

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.chat_id is not None:
            result['ChatId'] = self.chat_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        if self.pv is not None:
            result['Pv'] = self.pv
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['Uv'] = self.uv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        if m.get('Pv') is not None:
            self.pv = m.get('Pv')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        return self


class ListLiveRoomsResponseBodyResult(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        live_list: List[ListLiveRoomsResponseBodyResultLiveList] = None,
        page_total: int = None,
        total_count: int = None,
    ):
        self.has_more = has_more
        self.live_list = live_list
        self.page_total = page_total
        self.total_count = total_count

    def validate(self):
        if self.live_list:
            for k in self.live_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['LiveList'] = []
        if self.live_list is not None:
            for k in self.live_list:
                result['LiveList'].append(k.to_map() if k else None)
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.live_list = []
        if m.get('LiveList') is not None:
            for k in m.get('LiveList'):
                temp_model = ListLiveRoomsResponseBodyResultLiveList()
                self.live_list.append(temp_model.from_map(k))
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLiveRoomsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListLiveRoomsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListLiveRoomsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListLiveRoomsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLiveRoomsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListLiveRoomsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLiveRoomsByIdRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id_list: List[str] = None,
    ):
        self.app_id = app_id
        self.live_id_list = live_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id_list is not None:
            result['LiveIdList'] = self.live_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveIdList') is not None:
            self.live_id_list = m.get('LiveIdList')
        return self


class ListLiveRoomsByIdShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id_list_shrink: str = None,
    ):
        self.app_id = app_id
        self.live_id_list_shrink = live_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id_list_shrink is not None:
            result['LiveIdList'] = self.live_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveIdList') is not None:
            self.live_id_list_shrink = m.get('LiveIdList')
        return self


class ListLiveRoomsByIdResponseBodyResultLiveList(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        anchor_nick: str = None,
        app_id: str = None,
        chat_id: str = None,
        cover_url: str = None,
        create_time: int = None,
        end_time: int = None,
        extension: Dict[str, str] = None,
        live_id: str = None,
        notice: str = None,
        online_count: int = None,
        pv: int = None,
        room_id: str = None,
        start_time: int = None,
        status: int = None,
        title: str = None,
        uv: int = None,
    ):
        self.anchor_id = anchor_id
        self.anchor_nick = anchor_nick
        self.app_id = app_id
        self.chat_id = chat_id
        self.cover_url = cover_url
        self.create_time = create_time
        self.end_time = end_time
        self.extension = extension
        self.live_id = live_id
        self.notice = notice
        self.online_count = online_count
        self.pv = pv
        self.room_id = room_id
        self.start_time = start_time
        self.status = status
        self.title = title
        self.uv = uv

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.chat_id is not None:
            result['ChatId'] = self.chat_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        if self.pv is not None:
            result['Pv'] = self.pv
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['Uv'] = self.uv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        if m.get('Pv') is not None:
            self.pv = m.get('Pv')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        return self


class ListLiveRoomsByIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        live_list: List[ListLiveRoomsByIdResponseBodyResultLiveList] = None,
    ):
        self.live_list = live_list

    def validate(self):
        if self.live_list:
            for k in self.live_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveList'] = []
        if self.live_list is not None:
            for k in self.live_list:
                result['LiveList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_list = []
        if m.get('LiveList') is not None:
            for k in m.get('LiveList'):
                temp_model = ListLiveRoomsByIdResponseBodyResultLiveList()
                self.live_list.append(temp_model.from_map(k))
        return self


class ListLiveRoomsByIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListLiveRoomsByIdResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListLiveRoomsByIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListLiveRoomsByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLiveRoomsByIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListLiveRoomsByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoomUsersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
        room_id: str = None,
    ):
        self.app_id = app_id
        self.page_number = page_number
        self.page_size = page_size
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class ListRoomUsersResponseBodyResultRoomUserList(TeaModel):
    def __init__(
        self,
        extension: Dict[str, str] = None,
        nick: str = None,
        user_id: str = None,
    ):
        self.extension = extension
        self.nick = nick
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListRoomUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        page_total: int = None,
        room_user_list: List[ListRoomUsersResponseBodyResultRoomUserList] = None,
        total_count: int = None,
    ):
        self.has_more = has_more
        self.page_total = page_total
        self.room_user_list = room_user_list
        self.total_count = total_count

    def validate(self):
        if self.room_user_list:
            for k in self.room_user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        result['RoomUserList'] = []
        if self.room_user_list is not None:
            for k in self.room_user_list:
                result['RoomUserList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        self.room_user_list = []
        if m.get('RoomUserList') is not None:
            for k in m.get('RoomUserList'):
                temp_model = ListRoomUsersResponseBodyResultRoomUserList()
                self.room_user_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRoomUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListRoomUsersResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListRoomUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListRoomUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRoomUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListRoomUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoomsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        extension: Dict[str, str] = None,
        plugin_id: str = None,
        plugin_type: str = None,
    ):
        self.create_time = create_time
        self.extension = extension
        self.plugin_id = plugin_id
        self.plugin_type = plugin_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        return self


class ListRoomsResponseBodyResultRoomInfoList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: str = None,
        extension: Dict[str, str] = None,
        notice: str = None,
        online_count: int = None,
        plugin_instance_info_list: List[ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList] = None,
        room_id: str = None,
        room_owner_id: str = None,
        template_id: str = None,
        title: str = None,
        uv: int = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.extension = extension
        self.notice = notice
        self.online_count = online_count
        self.plugin_instance_info_list = plugin_instance_info_list
        self.room_id = room_id
        self.room_owner_id = room_owner_id
        self.template_id = template_id
        self.title = title
        self.uv = uv

    def validate(self):
        if self.plugin_instance_info_list:
            for k in self.plugin_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['Uv'] = self.uv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        return self


class ListRoomsResponseBodyResult(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        page_total: int = None,
        room_info_list: List[ListRoomsResponseBodyResultRoomInfoList] = None,
        total_count: int = None,
    ):
        self.has_more = has_more
        self.page_total = page_total
        self.room_info_list = room_info_list
        self.total_count = total_count

    def validate(self):
        if self.room_info_list:
            for k in self.room_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        result['RoomInfoList'] = []
        if self.room_info_list is not None:
            for k in self.room_info_list:
                result['RoomInfoList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        self.room_info_list = []
        if m.get('RoomInfoList') is not None:
            for k in m.get('RoomInfoList'):
                temp_model = ListRoomsResponseBodyResultRoomInfoList()
                self.room_info_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRoomsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListRoomsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListRoomsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListRoomsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRoomsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListRoomsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSensitiveWordRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSensitiveWordResponseBodyResult(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        word_list: List[str] = None,
    ):
        self.total_count = total_count
        self.word_list = word_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.word_list is not None:
            result['WordList'] = self.word_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('WordList') is not None:
            self.word_list = m.get('WordList')
        return self


class ListSensitiveWordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListSensitiveWordResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListSensitiveWordResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListSensitiveWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSensitiveWordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListSensitiveWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishLiveRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        user_id: str = None,
    ):
        self.live_id = live_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class PublishLiveResponseBodyResult(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        live_id: str = None,
        live_url: str = None,
        push_url: str = None,
        status: str = None,
    ):
        self.anchor_id = anchor_id
        self.live_id = live_id
        self.live_url = live_url
        self.push_url = push_url
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PublishLiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: PublishLiveResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = PublishLiveResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class PublishLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishLiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = PublishLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishLiveRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.live_id = live_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class PublishLiveRoomResponseBodyResult(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        live_url: str = None,
        push_url: str = None,
    ):
        self.live_id = live_id
        self.live_url = live_url
        self.push_url = push_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        return self


class PublishLiveRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: PublishLiveRoomResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = PublishLiveRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class PublishLiveRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishLiveRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = PublishLiveRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveMemberRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        from_user_id: str = None,
        to_user_id: str = None,
    ):
        self.conference_id = conference_id
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
        return self


class RemoveMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class RemoveMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveMemberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RemoveMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCommentRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: str = None,
        extension: Dict[str, str] = None,
        room_id: str = None,
        sender_id: str = None,
        sender_nick: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.extension = extension
        self.room_id = room_id
        self.sender_id = sender_id
        self.sender_nick = sender_nick

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        return self


class SendCommentShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: str = None,
        extension_shrink: str = None,
        room_id: str = None,
        sender_id: str = None,
        sender_nick: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.extension_shrink = extension_shrink
        self.room_id = room_id
        self.sender_id = sender_id
        self.sender_nick = sender_nick

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        return self


class SendCommentResponseBodyResultCommentVO(TeaModel):
    def __init__(
        self,
        comment_id: str = None,
        content: str = None,
        create_at: int = None,
        extension: Dict[str, str] = None,
        sender_id: str = None,
        sender_nick: str = None,
    ):
        self.comment_id = comment_id
        self.content = content
        self.create_at = create_at
        self.extension = extension
        self.sender_id = sender_id
        self.sender_nick = sender_nick

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment_id is not None:
            result['CommentId'] = self.comment_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_at is not None:
            result['CreateAt'] = self.create_at
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommentId') is not None:
            self.comment_id = m.get('CommentId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateAt') is not None:
            self.create_at = m.get('CreateAt')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        return self


class SendCommentResponseBodyResult(TeaModel):
    def __init__(
        self,
        comment_vo: SendCommentResponseBodyResultCommentVO = None,
    ):
        self.comment_vo = comment_vo

    def validate(self):
        if self.comment_vo:
            self.comment_vo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment_vo is not None:
            result['CommentVO'] = self.comment_vo.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommentVO') is not None:
            temp_model = SendCommentResponseBodyResultCommentVO()
            self.comment_vo = temp_model.from_map(m['CommentVO'])
        return self


class SendCommentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: SendCommentResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = SendCommentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendCommentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendCommentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SendCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomMessageToAllRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        body: str = None,
        room_id: str = None,
    ):
        self.app_id = app_id
        self.body = body
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.body is not None:
            result['Body'] = self.body
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class SendCustomMessageToAllResponseBodyResult(TeaModel):
    def __init__(
        self,
        message_id: str = None,
    ):
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class SendCustomMessageToAllResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: SendCustomMessageToAllResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = SendCustomMessageToAllResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendCustomMessageToAllResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendCustomMessageToAllResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SendCustomMessageToAllResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomMessageToUsersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        body: str = None,
        receiver_list: List[str] = None,
        room_id: str = None,
    ):
        self.app_id = app_id
        self.body = body
        self.receiver_list = receiver_list
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.body is not None:
            result['Body'] = self.body
        if self.receiver_list is not None:
            result['ReceiverList'] = self.receiver_list
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ReceiverList') is not None:
            self.receiver_list = m.get('ReceiverList')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class SendCustomMessageToUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        message_id: str = None,
    ):
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class SendCustomMessageToUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: SendCustomMessageToUsersResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = SendCustomMessageToUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendCustomMessageToUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendCustomMessageToUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SendCustomMessageToUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserAdminRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.room_id = room_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SetUserAdminResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class SetUserAdminResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetUserAdminResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetUserAdminResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopClassRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        class_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.class_id = class_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class StopClassResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class StopClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopClassResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StopClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLiveRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id: str = None,
        room_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.live_id = live_id
        self.room_id = room_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class StopLiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class StopLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopLiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StopLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLiveRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.live_id = live_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class StopLiveRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class StopLiveRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopLiveRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StopLiveRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClassRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        class_id: str = None,
        create_nickname: str = None,
        create_user_id: str = None,
        title: str = None,
    ):
        self.app_id = app_id
        self.class_id = class_id
        self.create_nickname = create_nickname
        self.create_user_id = create_user_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.create_nickname is not None:
            result['CreateNickname'] = self.create_nickname
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('CreateNickname') is not None:
            self.create_nickname = m.get('CreateNickname')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateClassResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class UpdateClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateClassResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLiveRequest(TeaModel):
    def __init__(
        self,
        introduction: str = None,
        live_id: str = None,
        title: str = None,
    ):
        self.introduction = introduction
        self.live_id = live_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateLiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class UpdateLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLiveRoomRequest(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        anchor_nick: str = None,
        app_id: str = None,
        cover_url: str = None,
        extension: Dict[str, str] = None,
        live_id: str = None,
        notice: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.anchor_id = anchor_id
        self.anchor_nick = anchor_nick
        self.app_id = app_id
        self.cover_url = cover_url
        self.extension = extension
        self.live_id = live_id
        self.notice = notice
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateLiveRoomShrinkRequest(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        anchor_nick: str = None,
        app_id: str = None,
        cover_url: str = None,
        extension_shrink: str = None,
        live_id: str = None,
        notice: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.anchor_id = anchor_id
        self.anchor_nick = anchor_nick
        self.app_id = app_id
        self.cover_url = cover_url
        self.extension_shrink = extension_shrink
        self.live_id = live_id
        self.notice = notice
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateLiveRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class UpdateLiveRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLiveRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateLiveRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        extension: Dict[str, str] = None,
        notice: str = None,
        room_id: str = None,
        room_owner_id: str = None,
        title: str = None,
    ):
        self.app_id = app_id
        self.extension = extension
        self.notice = notice
        self.room_id = room_id
        self.room_owner_id = room_owner_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateRoomShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        extension_shrink: str = None,
        notice: str = None,
        room_id: str = None,
        room_owner_id: str = None,
        title: str = None,
    ):
        self.app_id = app_id
        self.extension_shrink = extension_shrink
        self.notice = notice
        self.room_id = room_id
        self.room_owner_id = room_owner_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class UpdateRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateShareScreenLayoutRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        class_id: str = None,
        enable_overlay: bool = None,
        overlay_height: float = None,
        overlay_width: float = None,
        overlay_x: float = None,
        overlay_y: float = None,
    ):
        self.app_id = app_id
        self.class_id = class_id
        self.enable_overlay = enable_overlay
        self.overlay_height = overlay_height
        self.overlay_width = overlay_width
        self.overlay_x = overlay_x
        self.overlay_y = overlay_y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.enable_overlay is not None:
            result['EnableOverlay'] = self.enable_overlay
        if self.overlay_height is not None:
            result['OverlayHeight'] = self.overlay_height
        if self.overlay_width is not None:
            result['OverlayWidth'] = self.overlay_width
        if self.overlay_x is not None:
            result['OverlayX'] = self.overlay_x
        if self.overlay_y is not None:
            result['OverlayY'] = self.overlay_y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('EnableOverlay') is not None:
            self.enable_overlay = m.get('EnableOverlay')
        if m.get('OverlayHeight') is not None:
            self.overlay_height = m.get('OverlayHeight')
        if m.get('OverlayWidth') is not None:
            self.overlay_width = m.get('OverlayWidth')
        if m.get('OverlayX') is not None:
            self.overlay_x = m.get('OverlayX')
        if m.get('OverlayY') is not None:
            self.overlay_y = m.get('OverlayY')
        return self


class UpdateShareScreenLayoutResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class UpdateShareScreenLayoutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateShareScreenLayoutResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateShareScreenLayoutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


