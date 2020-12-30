# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ActivatePhotosRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class ActivatePhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ActivatePhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[ActivatePhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ActivatePhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ActivatePhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ActivatePhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ActivatePhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddAlbumPhotosRequest(TeaModel):
    def __init__(
        self,
        album_id: int = None,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.album_id = album_id
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class AddAlbumPhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class AddAlbumPhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[AddAlbumPhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AddAlbumPhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddAlbumPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAlbumPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAlbumPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlbumRequest(TeaModel):
    def __init__(
        self,
        album_name: str = None,
        store_name: str = None,
        remark: str = None,
        library_id: str = None,
    ):
        self.album_name = album_name
        self.store_name = store_name
        self.remark = remark
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class CreateAlbumResponseBodyAlbumCover(TeaModel):
    def __init__(
        self,
        remark: str = None,
        state: str = None,
        height: int = None,
        file_id: str = None,
        id_str: str = None,
        mtime: int = None,
        ctime: int = None,
        width: int = None,
        md_5: str = None,
        is_video: bool = None,
        title: str = None,
        id: int = None,
    ):
        self.remark = remark
        self.state = state
        self.height = height
        self.file_id = file_id
        self.id_str = id_str
        self.mtime = mtime
        self.ctime = ctime
        self.width = width
        self.md_5 = md_5
        self.is_video = is_video
        self.title = title
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.width is not None:
            result['Width'] = self.width
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.title is not None:
            result['Title'] = self.title
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateAlbumResponseBodyAlbum(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        photos_count: int = None,
        cover: CreateAlbumResponseBodyAlbumCover = None,
        mtime: int = None,
        ctime: int = None,
        remark: str = None,
        state: str = None,
        name: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.photos_count = photos_count
        self.cover = cover
        self.mtime = mtime
        self.ctime = ctime
        self.remark = remark
        self.state = state
        self.name = name
        self.id = id

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.photos_count is not None:
            result['PhotosCount'] = self.photos_count
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.state is not None:
            result['State'] = self.state
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('PhotosCount') is not None:
            self.photos_count = m.get('PhotosCount')
        if m.get('Cover') is not None:
            temp_model = CreateAlbumResponseBodyAlbumCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateAlbumResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        album: CreateAlbumResponseBodyAlbum = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.album = album
        self.code = code

    def validate(self):
        if self.album:
            self.album.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.album is not None:
            result['Album'] = self.album.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Album') is not None:
            temp_model = CreateAlbumResponseBodyAlbum()
            self.album = temp_model.from_map(m['Album'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateAlbumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAlbumResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAlbumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePhotoRequest(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        session_id: str = None,
        upload_type: str = None,
        photo_title: str = None,
        store_name: str = None,
        remark: str = None,
        library_id: str = None,
        staging: str = None,
        share_expire_time: int = None,
        taken_at: int = None,
    ):
        self.file_id = file_id
        self.session_id = session_id
        self.upload_type = upload_type
        self.photo_title = photo_title
        self.store_name = store_name
        self.remark = remark
        self.library_id = library_id
        self.staging = staging
        self.share_expire_time = share_expire_time
        self.taken_at = taken_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.photo_title is not None:
            result['PhotoTitle'] = self.photo_title
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.staging is not None:
            result['Staging'] = self.staging
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('PhotoTitle') is not None:
            self.photo_title = m.get('PhotoTitle')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('Staging') is not None:
            self.staging = m.get('Staging')
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        return self


class CreatePhotoResponseBodyPhoto(TeaModel):
    def __init__(
        self,
        remark: str = None,
        taken_at: int = None,
        state: str = None,
        height: int = None,
        share_expire_time: int = None,
        file_id: str = None,
        id_str: str = None,
        ctime: int = None,
        mtime: int = None,
        width: int = None,
        size: int = None,
        md_5: str = None,
        title: str = None,
        is_video: bool = None,
        id: int = None,
        location: str = None,
    ):
        self.remark = remark
        self.taken_at = taken_at
        self.state = state
        self.height = height
        self.share_expire_time = share_expire_time
        self.file_id = file_id
        self.id_str = id_str
        self.ctime = ctime
        self.mtime = mtime
        self.width = width
        self.size = size
        self.md_5 = md_5
        self.title = title
        self.is_video = is_video
        self.id = id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.width is not None:
            result['Width'] = self.width
        if self.size is not None:
            result['Size'] = self.size
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.title is not None:
            result['Title'] = self.title
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class CreatePhotoResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        photo: CreatePhotoResponseBodyPhoto = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.photo = photo
        self.code = code

    def validate(self):
        if self.photo:
            self.photo.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.photo is not None:
            result['Photo'] = self.photo.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Photo') is not None:
            temp_model = CreatePhotoResponseBodyPhoto()
            self.photo = temp_model.from_map(m['Photo'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreatePhotoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePhotoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePhotoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePhotoStoreRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        default_quota: int = None,
        bucket_name: str = None,
        remark: str = None,
    ):
        self.store_name = store_name
        self.default_quota = default_quota
        self.bucket_name = bucket_name
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.default_quota is not None:
            result['DefaultQuota'] = self.default_quota
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('DefaultQuota') is not None:
            self.default_quota = m.get('DefaultQuota')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class CreatePhotoStoreResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreatePhotoStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePhotoStoreResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePhotoStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransactionRequest(TeaModel):
    def __init__(
        self,
        size: int = None,
        ext: str = None,
        force: str = None,
        md_5: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.size = size
        self.ext = ext
        self.force = force
        self.md_5 = md_5
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.force is not None:
            result['Force'] = self.force
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class CreateTransactionResponseBodyTransactionUpload(TeaModel):
    def __init__(
        self,
        object_key: str = None,
        access_key_secret: str = None,
        session_id: str = None,
        access_key_id: str = None,
        sts_token: str = None,
        oss_endpoint: str = None,
        bucket: str = None,
        file_id: str = None,
    ):
        self.object_key = object_key
        self.access_key_secret = access_key_secret
        self.session_id = session_id
        self.access_key_id = access_key_id
        self.sts_token = sts_token
        self.oss_endpoint = oss_endpoint
        self.bucket = bucket
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.sts_token is not None:
            result['StsToken'] = self.sts_token
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('StsToken') is not None:
            self.sts_token = m.get('StsToken')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class CreateTransactionResponseBodyTransaction(TeaModel):
    def __init__(
        self,
        upload: CreateTransactionResponseBodyTransactionUpload = None,
    ):
        self.upload = upload

    def validate(self):
        if self.upload:
            self.upload.validate()

    def to_map(self):
        result = dict()
        if self.upload is not None:
            result['Upload'] = self.upload.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Upload') is not None:
            temp_model = CreateTransactionResponseBodyTransactionUpload()
            self.upload = temp_model.from_map(m['Upload'])
        return self


class CreateTransactionResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        transaction: CreateTransactionResponseBodyTransaction = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.transaction = transaction
        self.code = code

    def validate(self):
        if self.transaction:
            self.transaction.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transaction is not None:
            result['Transaction'] = self.transaction.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Transaction') is not None:
            temp_model = CreateTransactionResponseBodyTransaction()
            self.transaction = temp_model.from_map(m['Transaction'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateTransactionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTransactionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTransactionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlbumsRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        library_id: str = None,
        album_id: List[int] = None,
    ):
        self.store_name = store_name
        self.library_id = library_id
        self.album_id = album_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        return self


class DeleteAlbumsResponseBodyResults(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteAlbumsResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[DeleteAlbumsResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DeleteAlbumsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteAlbumsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAlbumsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAlbumsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventRequest(TeaModel):
    def __init__(
        self,
        event_id: int = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.event_id = event_id
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class DeleteEventResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEventResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFacesRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        library_id: str = None,
        face_id: List[int] = None,
    ):
        self.store_name = store_name
        self.library_id = library_id
        self.face_id = face_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        return self


class DeleteFacesResponseBodyResults(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteFacesResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[DeleteFacesResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DeleteFacesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePhotosRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class DeletePhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeletePhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[DeletePhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DeletePhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeletePhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeletePhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePhotoStoreRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
    ):
        self.store_name = store_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        return self


class DeletePhotoStoreResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeletePhotoStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePhotoStoreResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeletePhotoStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditPhotosRequest(TeaModel):
    def __init__(
        self,
        share_expire_time: int = None,
        taken_at: int = None,
        title: str = None,
        remark: str = None,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.share_expire_time = share_expire_time
        self.taken_at = taken_at
        self.title = title
        self.remark = remark
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.title is not None:
            result['Title'] = self.title
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class EditPhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class EditPhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[EditPhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = EditPhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class EditPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EditPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditPhotoStoreRequest(TeaModel):
    def __init__(
        self,
        auto_clean_enabled: str = None,
        auto_clean_days: int = None,
        default_quota: int = None,
        default_trash_quota: int = None,
        remark: str = None,
        store_name: str = None,
    ):
        self.auto_clean_enabled = auto_clean_enabled
        self.auto_clean_days = auto_clean_days
        self.default_quota = default_quota
        self.default_trash_quota = default_trash_quota
        self.remark = remark
        self.store_name = store_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auto_clean_enabled is not None:
            result['AutoCleanEnabled'] = self.auto_clean_enabled
        if self.auto_clean_days is not None:
            result['AutoCleanDays'] = self.auto_clean_days
        if self.default_quota is not None:
            result['DefaultQuota'] = self.default_quota
        if self.default_trash_quota is not None:
            result['DefaultTrashQuota'] = self.default_trash_quota
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCleanEnabled') is not None:
            self.auto_clean_enabled = m.get('AutoCleanEnabled')
        if m.get('AutoCleanDays') is not None:
            self.auto_clean_days = m.get('AutoCleanDays')
        if m.get('DefaultQuota') is not None:
            self.default_quota = m.get('DefaultQuota')
        if m.get('DefaultTrashQuota') is not None:
            self.default_trash_quota = m.get('DefaultTrashQuota')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        return self


class EditPhotoStoreResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class EditPhotoStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditPhotoStoreResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EditPhotoStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchAlbumTagPhotosRequest(TeaModel):
    def __init__(
        self,
        album_id: int = None,
        tag_id: int = None,
        size: int = None,
        page: int = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.album_id = album_id
        self.tag_id = tag_id
        self.size = size
        self.page = page
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.size is not None:
            result['Size'] = self.size
        if self.page is not None:
            result['Page'] = self.page
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class FetchAlbumTagPhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        photo_id_str: str = None,
        mtime: int = None,
        state: str = None,
        photo_id: int = None,
    ):
        self.photo_id_str = photo_id_str
        self.mtime = mtime
        self.state = state
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id_str is not None:
            result['PhotoIdStr'] = self.photo_id_str
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.state is not None:
            result['State'] = self.state
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoIdStr') is not None:
            self.photo_id_str = m.get('PhotoIdStr')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class FetchAlbumTagPhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        total_count: int = None,
        message: str = None,
        request_id: str = None,
        results: List[FetchAlbumTagPhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.total_count = total_count
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = FetchAlbumTagPhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class FetchAlbumTagPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FetchAlbumTagPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FetchAlbumTagPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchLibrariesRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        page: int = None,
        size: int = None,
        need_quota: bool = None,
    ):
        self.store_name = store_name
        self.page = page
        self.size = size
        self.need_quota = need_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.need_quota is not None:
            result['NeedQuota'] = self.need_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('NeedQuota') is not None:
            self.need_quota = m.get('NeedQuota')
        return self


class FetchLibrariesResponseBodyLibraries(TeaModel):
    def __init__(
        self,
        ctime: int = None,
        library_id: str = None,
        total_quota: int = None,
    ):
        self.ctime = ctime
        self.library_id = library_id
        self.total_quota = total_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        return self


class FetchLibrariesResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        total_count: int = None,
        message: str = None,
        request_id: str = None,
        libraries: List[FetchLibrariesResponseBodyLibraries] = None,
        code: str = None,
    ):
        self.action = action
        self.total_count = total_count
        self.message = message
        self.request_id = request_id
        self.libraries = libraries
        self.code = code

    def validate(self):
        if self.libraries:
            for k in self.libraries:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Libraries'] = []
        if self.libraries is not None:
            for k in self.libraries:
                result['Libraries'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.libraries = []
        if m.get('Libraries') is not None:
            for k in m.get('Libraries'):
                temp_model = FetchLibrariesResponseBodyLibraries()
                self.libraries.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class FetchLibrariesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FetchLibrariesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FetchLibrariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchMomentPhotosRequest(TeaModel):
    def __init__(
        self,
        moment_id: int = None,
        order_by: str = None,
        order: str = None,
        size: int = None,
        page: int = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.moment_id = moment_id
        self.order_by = order_by
        self.order = order
        self.size = size
        self.page = page
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.moment_id is not None:
            result['MomentId'] = self.moment_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order is not None:
            result['Order'] = self.order
        if self.size is not None:
            result['Size'] = self.size
        if self.page is not None:
            result['Page'] = self.page
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MomentId') is not None:
            self.moment_id = m.get('MomentId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class FetchMomentPhotosResponseBodyPhotos(TeaModel):
    def __init__(
        self,
        remark: str = None,
        taken_at: int = None,
        state: str = None,
        height: int = None,
        share_expire_time: int = None,
        file_id: str = None,
        id_str: str = None,
        ctime: int = None,
        mtime: int = None,
        size: int = None,
        width: int = None,
        inactive_time: int = None,
        md_5: str = None,
        is_video: bool = None,
        title: str = None,
        location: str = None,
        id: int = None,
    ):
        self.remark = remark
        self.taken_at = taken_at
        self.state = state
        self.height = height
        self.share_expire_time = share_expire_time
        self.file_id = file_id
        self.id_str = id_str
        self.ctime = ctime
        self.mtime = mtime
        self.size = size
        self.width = width
        self.inactive_time = inactive_time
        self.md_5 = md_5
        self.is_video = is_video
        self.title = title
        self.location = location
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.size is not None:
            result['Size'] = self.size
        if self.width is not None:
            result['Width'] = self.width
        if self.inactive_time is not None:
            result['InactiveTime'] = self.inactive_time
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.title is not None:
            result['Title'] = self.title
        if self.location is not None:
            result['Location'] = self.location
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('InactiveTime') is not None:
            self.inactive_time = m.get('InactiveTime')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FetchMomentPhotosResponseBody(TeaModel):
    def __init__(
        self,
        photos: List[FetchMomentPhotosResponseBodyPhotos] = None,
        action: str = None,
        total_count: int = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.photos = photos
        self.action = action
        self.total_count = total_count
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.photos:
            for k in self.photos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Photos'] = []
        if self.photos is not None:
            for k in self.photos:
                result['Photos'].append(k.to_map() if k else None)
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.photos = []
        if m.get('Photos') is not None:
            for k in m.get('Photos'):
                temp_model = FetchMomentPhotosResponseBodyPhotos()
                self.photos.append(temp_model.from_map(k))
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class FetchMomentPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FetchMomentPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FetchMomentPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchPhotosRequest(TeaModel):
    def __init__(
        self,
        state: str = None,
        order_by: str = None,
        order: str = None,
        size: int = None,
        page: int = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.state = state
        self.order_by = order_by
        self.order = order
        self.size = size
        self.page = page
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order is not None:
            result['Order'] = self.order
        if self.size is not None:
            result['Size'] = self.size
        if self.page is not None:
            result['Page'] = self.page
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class FetchPhotosResponseBodyPhotos(TeaModel):
    def __init__(
        self,
        remark: str = None,
        taken_at: int = None,
        state: str = None,
        height: int = None,
        share_expire_time: int = None,
        file_id: str = None,
        id_str: str = None,
        ctime: int = None,
        mtime: int = None,
        size: int = None,
        width: int = None,
        inactive_time: int = None,
        md_5: str = None,
        is_video: bool = None,
        title: str = None,
        location: str = None,
        id: int = None,
    ):
        self.remark = remark
        self.taken_at = taken_at
        self.state = state
        self.height = height
        self.share_expire_time = share_expire_time
        self.file_id = file_id
        self.id_str = id_str
        self.ctime = ctime
        self.mtime = mtime
        self.size = size
        self.width = width
        self.inactive_time = inactive_time
        self.md_5 = md_5
        self.is_video = is_video
        self.title = title
        self.location = location
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.size is not None:
            result['Size'] = self.size
        if self.width is not None:
            result['Width'] = self.width
        if self.inactive_time is not None:
            result['InactiveTime'] = self.inactive_time
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.title is not None:
            result['Title'] = self.title
        if self.location is not None:
            result['Location'] = self.location
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('InactiveTime') is not None:
            self.inactive_time = m.get('InactiveTime')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FetchPhotosResponseBody(TeaModel):
    def __init__(
        self,
        photos: List[FetchPhotosResponseBodyPhotos] = None,
        action: str = None,
        total_count: int = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.photos = photos
        self.action = action
        self.total_count = total_count
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.photos:
            for k in self.photos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Photos'] = []
        if self.photos is not None:
            for k in self.photos:
                result['Photos'].append(k.to_map() if k else None)
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.photos = []
        if m.get('Photos') is not None:
            for k in m.get('Photos'):
                temp_model = FetchPhotosResponseBodyPhotos()
                self.photos.append(temp_model.from_map(k))
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class FetchPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FetchPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FetchPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlbumsByNamesRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        library_id: str = None,
        name: List[str] = None,
    ):
        self.store_name = store_name
        self.library_id = library_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetAlbumsByNamesResponseBodyAlbumsCover(TeaModel):
    def __init__(
        self,
        remark: str = None,
        state: str = None,
        height: int = None,
        file_id: str = None,
        id_str: str = None,
        mtime: int = None,
        ctime: int = None,
        width: int = None,
        md_5: str = None,
        is_video: bool = None,
        title: str = None,
        id: int = None,
    ):
        self.remark = remark
        self.state = state
        self.height = height
        self.file_id = file_id
        self.id_str = id_str
        self.mtime = mtime
        self.ctime = ctime
        self.width = width
        self.md_5 = md_5
        self.is_video = is_video
        self.title = title
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.width is not None:
            result['Width'] = self.width
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.title is not None:
            result['Title'] = self.title
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetAlbumsByNamesResponseBodyAlbums(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        photos_count: int = None,
        cover: GetAlbumsByNamesResponseBodyAlbumsCover = None,
        mtime: int = None,
        ctime: int = None,
        state: str = None,
        name: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.photos_count = photos_count
        self.cover = cover
        self.mtime = mtime
        self.ctime = ctime
        self.state = state
        self.name = name
        self.id = id

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.photos_count is not None:
            result['PhotosCount'] = self.photos_count
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.state is not None:
            result['State'] = self.state
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('PhotosCount') is not None:
            self.photos_count = m.get('PhotosCount')
        if m.get('Cover') is not None:
            temp_model = GetAlbumsByNamesResponseBodyAlbumsCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetAlbumsByNamesResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
        albums: List[GetAlbumsByNamesResponseBodyAlbums] = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code
        self.albums = albums

    def validate(self):
        if self.albums:
            for k in self.albums:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Albums'] = []
        if self.albums is not None:
            for k in self.albums:
                result['Albums'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.albums = []
        if m.get('Albums') is not None:
            for k in m.get('Albums'):
                temp_model = GetAlbumsByNamesResponseBodyAlbums()
                self.albums.append(temp_model.from_map(k))
        return self


class GetAlbumsByNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlbumsByNamesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAlbumsByNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        photo_id: int = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.photo_id = photo_id
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class GetDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
        download_url: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code
        self.download_url = download_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        return self


class GetDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDownloadUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDownloadUrlsRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class GetDownloadUrlsResponseBodyResultsResult(TeaModel):
    def __init__(
        self,
        photo_id_str: str = None,
        download_url: str = None,
        code: str = None,
        message: str = None,
        photo_id: int = None,
    ):
        self.photo_id_str = photo_id_str
        self.download_url = download_url
        self.code = code
        self.message = message
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id_str is not None:
            result['PhotoIdStr'] = self.photo_id_str
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoIdStr') is not None:
            self.photo_id_str = m.get('PhotoIdStr')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class GetDownloadUrlsResponseBodyResults(TeaModel):
    def __init__(
        self,
        result: List[GetDownloadUrlsResponseBodyResultsResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetDownloadUrlsResponseBodyResultsResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetDownloadUrlsResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: GetDownloadUrlsResponseBodyResults = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.results is not None:
            result['Results'] = self.results.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Results') is not None:
            temp_model = GetDownloadUrlsResponseBodyResults()
            self.results = temp_model.from_map(m['Results'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetDownloadUrlsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDownloadUrlsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDownloadUrlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFramedPhotoUrlsRequest(TeaModel):
    def __init__(
        self,
        frame_id: str = None,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.frame_id = frame_id
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.frame_id is not None:
            result['FrameId'] = self.frame_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameId') is not None:
            self.frame_id = m.get('FrameId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class GetFramedPhotoUrlsResponseBodyResultsResult(TeaModel):
    def __init__(
        self,
        photo_id_str: str = None,
        framed_photo_url: str = None,
        code: str = None,
        message: str = None,
        photo_id: int = None,
    ):
        self.photo_id_str = photo_id_str
        self.framed_photo_url = framed_photo_url
        self.code = code
        self.message = message
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id_str is not None:
            result['PhotoIdStr'] = self.photo_id_str
        if self.framed_photo_url is not None:
            result['FramedPhotoUrl'] = self.framed_photo_url
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoIdStr') is not None:
            self.photo_id_str = m.get('PhotoIdStr')
        if m.get('FramedPhotoUrl') is not None:
            self.framed_photo_url = m.get('FramedPhotoUrl')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class GetFramedPhotoUrlsResponseBodyResults(TeaModel):
    def __init__(
        self,
        result: List[GetFramedPhotoUrlsResponseBodyResultsResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetFramedPhotoUrlsResponseBodyResultsResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetFramedPhotoUrlsResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: GetFramedPhotoUrlsResponseBodyResults = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.results is not None:
            result['Results'] = self.results.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Results') is not None:
            temp_model = GetFramedPhotoUrlsResponseBodyResults()
            self.results = temp_model.from_map(m['Results'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetFramedPhotoUrlsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFramedPhotoUrlsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFramedPhotoUrlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLibraryRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        library_id: str = None,
    ):
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class GetLibraryResponseBodyLibraryAutoCleanConfig(TeaModel):
    def __init__(
        self,
        auto_clean_days: int = None,
        auto_clean_enabled: bool = None,
    ):
        self.auto_clean_days = auto_clean_days
        self.auto_clean_enabled = auto_clean_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auto_clean_days is not None:
            result['AutoCleanDays'] = self.auto_clean_days
        if self.auto_clean_enabled is not None:
            result['AutoCleanEnabled'] = self.auto_clean_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCleanDays') is not None:
            self.auto_clean_days = m.get('AutoCleanDays')
        if m.get('AutoCleanEnabled') is not None:
            self.auto_clean_enabled = m.get('AutoCleanEnabled')
        return self


class GetLibraryResponseBodyLibraryQuota(TeaModel):
    def __init__(
        self,
        photos_count: int = None,
        total_trash_quota: int = None,
        inactive_size: int = None,
        active_size: int = None,
        faces_count: int = None,
        videos_count: int = None,
        used_quota: int = None,
        total_quota: int = None,
    ):
        self.photos_count = photos_count
        self.total_trash_quota = total_trash_quota
        self.inactive_size = inactive_size
        self.active_size = active_size
        self.faces_count = faces_count
        self.videos_count = videos_count
        self.used_quota = used_quota
        self.total_quota = total_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photos_count is not None:
            result['PhotosCount'] = self.photos_count
        if self.total_trash_quota is not None:
            result['TotalTrashQuota'] = self.total_trash_quota
        if self.inactive_size is not None:
            result['InactiveSize'] = self.inactive_size
        if self.active_size is not None:
            result['ActiveSize'] = self.active_size
        if self.faces_count is not None:
            result['FacesCount'] = self.faces_count
        if self.videos_count is not None:
            result['VideosCount'] = self.videos_count
        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotosCount') is not None:
            self.photos_count = m.get('PhotosCount')
        if m.get('TotalTrashQuota') is not None:
            self.total_trash_quota = m.get('TotalTrashQuota')
        if m.get('InactiveSize') is not None:
            self.inactive_size = m.get('InactiveSize')
        if m.get('ActiveSize') is not None:
            self.active_size = m.get('ActiveSize')
        if m.get('FacesCount') is not None:
            self.faces_count = m.get('FacesCount')
        if m.get('VideosCount') is not None:
            self.videos_count = m.get('VideosCount')
        if m.get('UsedQuota') is not None:
            self.used_quota = m.get('UsedQuota')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        return self


class GetLibraryResponseBodyLibrary(TeaModel):
    def __init__(
        self,
        auto_clean_config: GetLibraryResponseBodyLibraryAutoCleanConfig = None,
        quota: GetLibraryResponseBodyLibraryQuota = None,
        ctime: int = None,
    ):
        self.auto_clean_config = auto_clean_config
        self.quota = quota
        self.ctime = ctime

    def validate(self):
        if self.auto_clean_config:
            self.auto_clean_config.validate()
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        if self.auto_clean_config is not None:
            result['AutoCleanConfig'] = self.auto_clean_config.to_map()
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCleanConfig') is not None:
            temp_model = GetLibraryResponseBodyLibraryAutoCleanConfig()
            self.auto_clean_config = temp_model.from_map(m['AutoCleanConfig'])
        if m.get('Quota') is not None:
            temp_model = GetLibraryResponseBodyLibraryQuota()
            self.quota = temp_model.from_map(m['Quota'])
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        return self


class GetLibraryResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        library: GetLibraryResponseBodyLibrary = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.library = library
        self.code = code

    def validate(self):
        if self.library:
            self.library.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.library is not None:
            result['Library'] = self.library.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Library') is not None:
            temp_model = GetLibraryResponseBodyLibrary()
            self.library = temp_model.from_map(m['Library'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetLibraryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLibraryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLibraryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhotosRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class GetPhotosResponseBodyPhotos(TeaModel):
    def __init__(
        self,
        remark: str = None,
        taken_at: int = None,
        state: str = None,
        height: int = None,
        share_expire_time: int = None,
        file_id: str = None,
        id_str: str = None,
        ctime: int = None,
        mtime: int = None,
        width: int = None,
        size: int = None,
        inactive_time: int = None,
        md_5: str = None,
        is_video: bool = None,
        title: str = None,
        like: int = None,
        location: str = None,
        id: int = None,
    ):
        self.remark = remark
        self.taken_at = taken_at
        self.state = state
        self.height = height
        self.share_expire_time = share_expire_time
        self.file_id = file_id
        self.id_str = id_str
        self.ctime = ctime
        self.mtime = mtime
        self.width = width
        self.size = size
        self.inactive_time = inactive_time
        self.md_5 = md_5
        self.is_video = is_video
        self.title = title
        self.like = like
        self.location = location
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.width is not None:
            result['Width'] = self.width
        if self.size is not None:
            result['Size'] = self.size
        if self.inactive_time is not None:
            result['InactiveTime'] = self.inactive_time
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.title is not None:
            result['Title'] = self.title
        if self.like is not None:
            result['Like'] = self.like
        if self.location is not None:
            result['Location'] = self.location
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('InactiveTime') is not None:
            self.inactive_time = m.get('InactiveTime')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Like') is not None:
            self.like = m.get('Like')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetPhotosResponseBody(TeaModel):
    def __init__(
        self,
        photos: List[GetPhotosResponseBodyPhotos] = None,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.photos = photos
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.photos:
            for k in self.photos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Photos'] = []
        if self.photos is not None:
            for k in self.photos:
                result['Photos'].append(k.to_map() if k else None)
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.photos = []
        if m.get('Photos') is not None:
            for k in m.get('Photos'):
                temp_model = GetPhotosResponseBodyPhotos()
                self.photos.append(temp_model.from_map(k))
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhotosByMd5sRequest(TeaModel):
    def __init__(
        self,
        state: str = None,
        store_name: str = None,
        library_id: str = None,
        md_5: List[str] = None,
    ):
        self.state = state
        self.store_name = store_name
        self.library_id = library_id
        self.md_5 = md_5

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        return self


class GetPhotosByMd5sResponseBodyPhotos(TeaModel):
    def __init__(
        self,
        remark: str = None,
        taken_at: int = None,
        state: str = None,
        height: int = None,
        share_expire_time: int = None,
        file_id: str = None,
        id_str: str = None,
        ctime: int = None,
        mtime: int = None,
        width: int = None,
        size: int = None,
        md_5: str = None,
        title: str = None,
        is_video: bool = None,
        id: int = None,
        location: str = None,
    ):
        self.remark = remark
        self.taken_at = taken_at
        self.state = state
        self.height = height
        self.share_expire_time = share_expire_time
        self.file_id = file_id
        self.id_str = id_str
        self.ctime = ctime
        self.mtime = mtime
        self.width = width
        self.size = size
        self.md_5 = md_5
        self.title = title
        self.is_video = is_video
        self.id = id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.width is not None:
            result['Width'] = self.width
        if self.size is not None:
            result['Size'] = self.size
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.title is not None:
            result['Title'] = self.title
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class GetPhotosByMd5sResponseBody(TeaModel):
    def __init__(
        self,
        photos: List[GetPhotosByMd5sResponseBodyPhotos] = None,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.photos = photos
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.photos:
            for k in self.photos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Photos'] = []
        if self.photos is not None:
            for k in self.photos:
                result['Photos'].append(k.to_map() if k else None)
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.photos = []
        if m.get('Photos') is not None:
            for k in m.get('Photos'):
                temp_model = GetPhotosByMd5sResponseBodyPhotos()
                self.photos.append(temp_model.from_map(k))
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetPhotosByMd5sResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPhotosByMd5sResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPhotosByMd5sResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhotoStoreRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
    ):
        self.store_name = store_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        return self


class GetPhotoStoreResponseBodyPhotoStoreBuckets(TeaModel):
    def __init__(
        self,
        acl: str = None,
        state: str = None,
        region: str = None,
        name: str = None,
    ):
        self.acl = acl
        self.state = state
        self.region = region
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.acl is not None:
            result['Acl'] = self.acl
        if self.state is not None:
            result['State'] = self.state
        if self.region is not None:
            result['Region'] = self.region
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acl') is not None:
            self.acl = m.get('Acl')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetPhotoStoreResponseBodyPhotoStore(TeaModel):
    def __init__(
        self,
        auto_clean_days: int = None,
        id_str: str = None,
        mtime: int = None,
        ctime: int = None,
        default_trash_quota: int = None,
        remark: str = None,
        buckets: List[GetPhotoStoreResponseBodyPhotoStoreBuckets] = None,
        default_quota: int = None,
        name: str = None,
        auto_clean_enabled: bool = None,
        id: int = None,
    ):
        self.auto_clean_days = auto_clean_days
        self.id_str = id_str
        self.mtime = mtime
        self.ctime = ctime
        self.default_trash_quota = default_trash_quota
        self.remark = remark
        self.buckets = buckets
        self.default_quota = default_quota
        self.name = name
        self.auto_clean_enabled = auto_clean_enabled
        self.id = id

    def validate(self):
        if self.buckets:
            for k in self.buckets:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auto_clean_days is not None:
            result['AutoCleanDays'] = self.auto_clean_days
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.default_trash_quota is not None:
            result['DefaultTrashQuota'] = self.default_trash_quota
        if self.remark is not None:
            result['Remark'] = self.remark
        result['Buckets'] = []
        if self.buckets is not None:
            for k in self.buckets:
                result['Buckets'].append(k.to_map() if k else None)
        if self.default_quota is not None:
            result['DefaultQuota'] = self.default_quota
        if self.name is not None:
            result['Name'] = self.name
        if self.auto_clean_enabled is not None:
            result['AutoCleanEnabled'] = self.auto_clean_enabled
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCleanDays') is not None:
            self.auto_clean_days = m.get('AutoCleanDays')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('DefaultTrashQuota') is not None:
            self.default_trash_quota = m.get('DefaultTrashQuota')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        self.buckets = []
        if m.get('Buckets') is not None:
            for k in m.get('Buckets'):
                temp_model = GetPhotoStoreResponseBodyPhotoStoreBuckets()
                self.buckets.append(temp_model.from_map(k))
        if m.get('DefaultQuota') is not None:
            self.default_quota = m.get('DefaultQuota')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AutoCleanEnabled') is not None:
            self.auto_clean_enabled = m.get('AutoCleanEnabled')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetPhotoStoreResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        photo_store: GetPhotoStoreResponseBodyPhotoStore = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.photo_store = photo_store
        self.code = code

    def validate(self):
        if self.photo_store:
            self.photo_store.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.photo_store is not None:
            result['PhotoStore'] = self.photo_store.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PhotoStore') is not None:
            temp_model = GetPhotoStoreResponseBodyPhotoStore()
            self.photo_store = temp_model.from_map(m['PhotoStore'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetPhotoStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPhotoStoreResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPhotoStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrivateAccessUrlsRequest(TeaModel):
    def __init__(
        self,
        zoom_type: str = None,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.zoom_type = zoom_type
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.zoom_type is not None:
            result['ZoomType'] = self.zoom_type
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoomType') is not None:
            self.zoom_type = m.get('ZoomType')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class GetPrivateAccessUrlsResponseBodyResults(TeaModel):
    def __init__(
        self,
        photo_id_str: str = None,
        code: str = None,
        message: str = None,
        photo_id: int = None,
        access_url: str = None,
    ):
        self.photo_id_str = photo_id_str
        self.code = code
        self.message = message
        self.photo_id = photo_id
        self.access_url = access_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id_str is not None:
            result['PhotoIdStr'] = self.photo_id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        if self.access_url is not None:
            result['AccessUrl'] = self.access_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoIdStr') is not None:
            self.photo_id_str = m.get('PhotoIdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        if m.get('AccessUrl') is not None:
            self.access_url = m.get('AccessUrl')
        return self


class GetPrivateAccessUrlsResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[GetPrivateAccessUrlsResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = GetPrivateAccessUrlsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetPrivateAccessUrlsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPrivateAccessUrlsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPrivateAccessUrlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicAccessUrlsRequest(TeaModel):
    def __init__(
        self,
        zoom_type: str = None,
        domain_type: str = None,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.zoom_type = zoom_type
        self.domain_type = domain_type
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.zoom_type is not None:
            result['ZoomType'] = self.zoom_type
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoomType') is not None:
            self.zoom_type = m.get('ZoomType')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class GetPublicAccessUrlsResponseBodyResults(TeaModel):
    def __init__(
        self,
        photo_id_str: str = None,
        code: str = None,
        message: str = None,
        photo_id: int = None,
        access_url: str = None,
    ):
        self.photo_id_str = photo_id_str
        self.code = code
        self.message = message
        self.photo_id = photo_id
        self.access_url = access_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id_str is not None:
            result['PhotoIdStr'] = self.photo_id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        if self.access_url is not None:
            result['AccessUrl'] = self.access_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoIdStr') is not None:
            self.photo_id_str = m.get('PhotoIdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        if m.get('AccessUrl') is not None:
            self.access_url = m.get('AccessUrl')
        return self


class GetPublicAccessUrlsResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[GetPublicAccessUrlsResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = GetPublicAccessUrlsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetPublicAccessUrlsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPublicAccessUrlsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPublicAccessUrlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        library_id: str = None,
    ):
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class GetQuotaResponseBodyQuota(TeaModel):
    def __init__(
        self,
        photos_count: int = None,
        videos_count: int = None,
        faces_count: int = None,
        used_quota: int = None,
        total_quota: int = None,
    ):
        self.photos_count = photos_count
        self.videos_count = videos_count
        self.faces_count = faces_count
        self.used_quota = used_quota
        self.total_quota = total_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photos_count is not None:
            result['PhotosCount'] = self.photos_count
        if self.videos_count is not None:
            result['VideosCount'] = self.videos_count
        if self.faces_count is not None:
            result['FacesCount'] = self.faces_count
        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotosCount') is not None:
            self.photos_count = m.get('PhotosCount')
        if m.get('VideosCount') is not None:
            self.videos_count = m.get('VideosCount')
        if m.get('FacesCount') is not None:
            self.faces_count = m.get('FacesCount')
        if m.get('UsedQuota') is not None:
            self.used_quota = m.get('UsedQuota')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        return self


class GetQuotaResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        quota: GetQuotaResponseBodyQuota = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.quota = quota
        self.code = code

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Quota') is not None:
            temp_model = GetQuotaResponseBodyQuota()
            self.quota = temp_model.from_map(m['Quota'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetQuotaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSimilarPhotosRequest(TeaModel):
    def __init__(
        self,
        photo_id: int = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.photo_id = photo_id
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class GetSimilarPhotosResponseBodyPhotos(TeaModel):
    def __init__(
        self,
        remark: str = None,
        taken_at: int = None,
        state: str = None,
        height: int = None,
        share_expire_time: int = None,
        file_id: str = None,
        id_str: str = None,
        ctime: int = None,
        mtime: int = None,
        size: int = None,
        width: int = None,
        inactive_time: int = None,
        md_5: str = None,
        is_video: bool = None,
        title: str = None,
        like: int = None,
        location: str = None,
        id: int = None,
    ):
        self.remark = remark
        self.taken_at = taken_at
        self.state = state
        self.height = height
        self.share_expire_time = share_expire_time
        self.file_id = file_id
        self.id_str = id_str
        self.ctime = ctime
        self.mtime = mtime
        self.size = size
        self.width = width
        self.inactive_time = inactive_time
        self.md_5 = md_5
        self.is_video = is_video
        self.title = title
        self.like = like
        self.location = location
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.size is not None:
            result['Size'] = self.size
        if self.width is not None:
            result['Width'] = self.width
        if self.inactive_time is not None:
            result['InactiveTime'] = self.inactive_time
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.title is not None:
            result['Title'] = self.title
        if self.like is not None:
            result['Like'] = self.like
        if self.location is not None:
            result['Location'] = self.location
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('InactiveTime') is not None:
            self.inactive_time = m.get('InactiveTime')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Like') is not None:
            self.like = m.get('Like')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetSimilarPhotosResponseBody(TeaModel):
    def __init__(
        self,
        photos: List[GetSimilarPhotosResponseBodyPhotos] = None,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.photos = photos
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.photos:
            for k in self.photos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Photos'] = []
        if self.photos is not None:
            for k in self.photos:
                result['Photos'].append(k.to_map() if k else None)
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.photos = []
        if m.get('Photos') is not None:
            for k in m.get('Photos'):
                temp_model = GetSimilarPhotosResponseBodyPhotos()
                self.photos.append(temp_model.from_map(k))
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetSimilarPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSimilarPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSimilarPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetThumbnailRequest(TeaModel):
    def __init__(
        self,
        photo_id: int = None,
        zoom_type: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.photo_id = photo_id
        self.zoom_type = zoom_type
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        if self.zoom_type is not None:
            result['ZoomType'] = self.zoom_type
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        if m.get('ZoomType') is not None:
            self.zoom_type = m.get('ZoomType')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class GetThumbnailResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        thumbnail_url: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.thumbnail_url = thumbnail_url
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetThumbnailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetThumbnailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetThumbnailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetThumbnailsRequest(TeaModel):
    def __init__(
        self,
        zoom_type: str = None,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.zoom_type = zoom_type
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.zoom_type is not None:
            result['ZoomType'] = self.zoom_type
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoomType') is not None:
            self.zoom_type = m.get('ZoomType')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class GetThumbnailsResponseBodyResultsResult(TeaModel):
    def __init__(
        self,
        thumbnail_url: str = None,
        photo_id_str: str = None,
        code: str = None,
        message: str = None,
        photo_id: int = None,
    ):
        self.thumbnail_url = thumbnail_url
        self.photo_id_str = photo_id_str
        self.code = code
        self.message = message
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url
        if self.photo_id_str is not None:
            result['PhotoIdStr'] = self.photo_id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')
        if m.get('PhotoIdStr') is not None:
            self.photo_id_str = m.get('PhotoIdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class GetThumbnailsResponseBodyResults(TeaModel):
    def __init__(
        self,
        result: List[GetThumbnailsResponseBodyResultsResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetThumbnailsResponseBodyResultsResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetThumbnailsResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: GetThumbnailsResponseBodyResults = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.results is not None:
            result['Results'] = self.results.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Results') is not None:
            temp_model = GetThumbnailsResponseBodyResults()
            self.results = temp_model.from_map(m['Results'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetThumbnailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetThumbnailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetThumbnailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoCoverRequest(TeaModel):
    def __init__(
        self,
        photo_id: int = None,
        zoom_type: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.photo_id = photo_id
        self.zoom_type = zoom_type
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        if self.zoom_type is not None:
            result['ZoomType'] = self.zoom_type
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        if m.get('ZoomType') is not None:
            self.zoom_type = m.get('ZoomType')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class GetVideoCoverResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        video_cover_url: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.video_cover_url = video_cover_url
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.video_cover_url is not None:
            result['VideoCoverUrl'] = self.video_cover_url
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VideoCoverUrl') is not None:
            self.video_cover_url = m.get('VideoCoverUrl')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetVideoCoverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVideoCoverResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVideoCoverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InactivatePhotosRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        library_id: str = None,
        inactive_time: int = None,
        photo_id: List[int] = None,
    ):
        self.store_name = store_name
        self.library_id = library_id
        self.inactive_time = inactive_time
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.inactive_time is not None:
            result['InactiveTime'] = self.inactive_time
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('InactiveTime') is not None:
            self.inactive_time = m.get('InactiveTime')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class InactivatePhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class InactivatePhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[InactivatePhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = InactivatePhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class InactivatePhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InactivatePhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InactivatePhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LikePhotoRequest(TeaModel):
    def __init__(
        self,
        photo_id: int = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.photo_id = photo_id
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class LikePhotoResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class LikePhotoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LikePhotoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LikePhotoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlbumPhotosRequest(TeaModel):
    def __init__(
        self,
        album_id: int = None,
        direction: str = None,
        size: int = None,
        cursor: str = None,
        state: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.album_id = album_id
        self.direction = direction
        self.size = size
        self.cursor = cursor
        self.state = state
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.size is not None:
            result['Size'] = self.size
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.state is not None:
            result['State'] = self.state
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class ListAlbumPhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        photo_id_str: str = None,
        mtime: int = None,
        state: str = None,
        photo_id: int = None,
    ):
        self.photo_id_str = photo_id_str
        self.mtime = mtime
        self.state = state
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id_str is not None:
            result['PhotoIdStr'] = self.photo_id_str
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.state is not None:
            result['State'] = self.state
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoIdStr') is not None:
            self.photo_id_str = m.get('PhotoIdStr')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class ListAlbumPhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        total_count: int = None,
        next_cursor: str = None,
        request_id: str = None,
        message: str = None,
        results: List[ListAlbumPhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.total_count = total_count
        self.next_cursor = next_cursor
        self.request_id = request_id
        self.message = message
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_cursor is not None:
            result['NextCursor'] = self.next_cursor
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextCursor') is not None:
            self.next_cursor = m.get('NextCursor')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ListAlbumPhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListAlbumPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlbumPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlbumPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlbumsRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        size: int = None,
        cursor: str = None,
        state: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.direction = direction
        self.size = size
        self.cursor = cursor
        self.state = state
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.size is not None:
            result['Size'] = self.size
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.state is not None:
            result['State'] = self.state
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class ListAlbumsResponseBodyAlbumsCover(TeaModel):
    def __init__(
        self,
        remark: str = None,
        state: str = None,
        height: int = None,
        file_id: str = None,
        id_str: str = None,
        mtime: int = None,
        ctime: int = None,
        width: int = None,
        md_5: str = None,
        is_video: bool = None,
        title: str = None,
        id: int = None,
    ):
        self.remark = remark
        self.state = state
        self.height = height
        self.file_id = file_id
        self.id_str = id_str
        self.mtime = mtime
        self.ctime = ctime
        self.width = width
        self.md_5 = md_5
        self.is_video = is_video
        self.title = title
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.width is not None:
            result['Width'] = self.width
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.title is not None:
            result['Title'] = self.title
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListAlbumsResponseBodyAlbums(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        photos_count: int = None,
        cover: ListAlbumsResponseBodyAlbumsCover = None,
        mtime: int = None,
        ctime: int = None,
        remark: str = None,
        state: str = None,
        name: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.photos_count = photos_count
        self.cover = cover
        self.mtime = mtime
        self.ctime = ctime
        self.remark = remark
        self.state = state
        self.name = name
        self.id = id

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.photos_count is not None:
            result['PhotosCount'] = self.photos_count
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.state is not None:
            result['State'] = self.state
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('PhotosCount') is not None:
            self.photos_count = m.get('PhotosCount')
        if m.get('Cover') is not None:
            temp_model = ListAlbumsResponseBodyAlbumsCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListAlbumsResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        total_count: int = None,
        next_cursor: str = None,
        request_id: str = None,
        message: str = None,
        code: str = None,
        albums: List[ListAlbumsResponseBodyAlbums] = None,
    ):
        self.action = action
        self.total_count = total_count
        self.next_cursor = next_cursor
        self.request_id = request_id
        self.message = message
        self.code = code
        self.albums = albums

    def validate(self):
        if self.albums:
            for k in self.albums:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_cursor is not None:
            result['NextCursor'] = self.next_cursor
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        result['Albums'] = []
        if self.albums is not None:
            for k in self.albums:
                result['Albums'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextCursor') is not None:
            self.next_cursor = m.get('NextCursor')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.albums = []
        if m.get('Albums') is not None:
            for k in m.get('Albums'):
                temp_model = ListAlbumsResponseBodyAlbums()
                self.albums.append(temp_model.from_map(k))
        return self


class ListAlbumsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlbumsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlbumsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFacePhotosRequest(TeaModel):
    def __init__(
        self,
        face_id: int = None,
        direction: str = None,
        size: int = None,
        cursor: str = None,
        state: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.face_id = face_id
        self.direction = direction
        self.size = size
        self.cursor = cursor
        self.state = state
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.size is not None:
            result['Size'] = self.size
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.state is not None:
            result['State'] = self.state
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class ListFacePhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        photo_id_str: str = None,
        mtime: int = None,
        state: str = None,
        photo_id: int = None,
    ):
        self.photo_id_str = photo_id_str
        self.mtime = mtime
        self.state = state
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id_str is not None:
            result['PhotoIdStr'] = self.photo_id_str
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.state is not None:
            result['State'] = self.state
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoIdStr') is not None:
            self.photo_id_str = m.get('PhotoIdStr')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class ListFacePhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        total_count: int = None,
        next_cursor: str = None,
        request_id: str = None,
        message: str = None,
        results: List[ListFacePhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.total_count = total_count
        self.next_cursor = next_cursor
        self.request_id = request_id
        self.message = message
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_cursor is not None:
            result['NextCursor'] = self.next_cursor
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextCursor') is not None:
            self.next_cursor = m.get('NextCursor')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ListFacePhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListFacePhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFacePhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFacePhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFacesRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        size: int = None,
        cursor: str = None,
        state: str = None,
        store_name: str = None,
        library_id: str = None,
        has_face_name: str = None,
    ):
        self.direction = direction
        self.size = size
        self.cursor = cursor
        self.state = state
        self.store_name = store_name
        self.library_id = library_id
        self.has_face_name = has_face_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.size is not None:
            result['Size'] = self.size
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.state is not None:
            result['State'] = self.state
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.has_face_name is not None:
            result['HasFaceName'] = self.has_face_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('HasFaceName') is not None:
            self.has_face_name = m.get('HasFaceName')
        return self


class ListFacesResponseBodyFacesCover(TeaModel):
    def __init__(
        self,
        remark: str = None,
        state: str = None,
        height: int = None,
        file_id: str = None,
        id_str: str = None,
        mtime: int = None,
        ctime: int = None,
        width: int = None,
        md_5: str = None,
        is_video: bool = None,
        title: str = None,
        id: int = None,
    ):
        self.remark = remark
        self.state = state
        self.height = height
        self.file_id = file_id
        self.id_str = id_str
        self.mtime = mtime
        self.ctime = ctime
        self.width = width
        self.md_5 = md_5
        self.is_video = is_video
        self.title = title
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.width is not None:
            result['Width'] = self.width
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.title is not None:
            result['Title'] = self.title
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListFacesResponseBodyFaces(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        photos_count: int = None,
        is_me: bool = None,
        cover: ListFacesResponseBodyFacesCover = None,
        mtime: int = None,
        ctime: int = None,
        state: str = None,
        axis: List[str] = None,
        name: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.photos_count = photos_count
        self.is_me = is_me
        self.cover = cover
        self.mtime = mtime
        self.ctime = ctime
        self.state = state
        self.axis = axis
        self.name = name
        self.id = id

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.photos_count is not None:
            result['PhotosCount'] = self.photos_count
        if self.is_me is not None:
            result['IsMe'] = self.is_me
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.state is not None:
            result['State'] = self.state
        if self.axis is not None:
            result['Axis'] = self.axis
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('PhotosCount') is not None:
            self.photos_count = m.get('PhotosCount')
        if m.get('IsMe') is not None:
            self.is_me = m.get('IsMe')
        if m.get('Cover') is not None:
            temp_model = ListFacesResponseBodyFacesCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Axis') is not None:
            self.axis = m.get('Axis')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListFacesResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        total_count: int = None,
        next_cursor: str = None,
        request_id: str = None,
        message: str = None,
        code: str = None,
        faces: List[ListFacesResponseBodyFaces] = None,
    ):
        self.action = action
        self.total_count = total_count
        self.next_cursor = next_cursor
        self.request_id = request_id
        self.message = message
        self.code = code
        self.faces = faces

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_cursor is not None:
            result['NextCursor'] = self.next_cursor
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextCursor') is not None:
            self.next_cursor = m.get('NextCursor')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = ListFacesResponseBodyFaces()
                self.faces.append(temp_model.from_map(k))
        return self


class ListFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMomentPhotosRequest(TeaModel):
    def __init__(
        self,
        moment_id: int = None,
        direction: str = None,
        size: int = None,
        cursor: str = None,
        state: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.moment_id = moment_id
        self.direction = direction
        self.size = size
        self.cursor = cursor
        self.state = state
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.moment_id is not None:
            result['MomentId'] = self.moment_id
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.size is not None:
            result['Size'] = self.size
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.state is not None:
            result['State'] = self.state
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MomentId') is not None:
            self.moment_id = m.get('MomentId')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class ListMomentPhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        photo_id_str: str = None,
        state: str = None,
        photo_id: int = None,
    ):
        self.photo_id_str = photo_id_str
        self.state = state
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id_str is not None:
            result['PhotoIdStr'] = self.photo_id_str
        if self.state is not None:
            result['State'] = self.state
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoIdStr') is not None:
            self.photo_id_str = m.get('PhotoIdStr')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class ListMomentPhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        total_count: int = None,
        next_cursor: str = None,
        request_id: str = None,
        message: str = None,
        results: List[ListMomentPhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.total_count = total_count
        self.next_cursor = next_cursor
        self.request_id = request_id
        self.message = message
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_cursor is not None:
            result['NextCursor'] = self.next_cursor
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextCursor') is not None:
            self.next_cursor = m.get('NextCursor')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ListMomentPhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListMomentPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMomentPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMomentPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMomentsRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        size: int = None,
        cursor: str = None,
        state: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.direction = direction
        self.size = size
        self.cursor = cursor
        self.state = state
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.size is not None:
            result['Size'] = self.size
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.state is not None:
            result['State'] = self.state
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class ListMomentsResponseBodyMoments(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        photos_count: int = None,
        mtime: int = None,
        ctime: int = None,
        taken_at: int = None,
        state: str = None,
        location_name: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.photos_count = photos_count
        self.mtime = mtime
        self.ctime = ctime
        self.taken_at = taken_at
        self.state = state
        self.location_name = location_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.photos_count is not None:
            result['PhotosCount'] = self.photos_count
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.state is not None:
            result['State'] = self.state
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('PhotosCount') is not None:
            self.photos_count = m.get('PhotosCount')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListMomentsResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        total_count: int = None,
        next_cursor: str = None,
        request_id: str = None,
        message: str = None,
        moments: List[ListMomentsResponseBodyMoments] = None,
        code: str = None,
    ):
        self.action = action
        self.total_count = total_count
        self.next_cursor = next_cursor
        self.request_id = request_id
        self.message = message
        self.moments = moments
        self.code = code

    def validate(self):
        if self.moments:
            for k in self.moments:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_cursor is not None:
            result['NextCursor'] = self.next_cursor
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        result['Moments'] = []
        if self.moments is not None:
            for k in self.moments:
                result['Moments'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextCursor') is not None:
            self.next_cursor = m.get('NextCursor')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.moments = []
        if m.get('Moments') is not None:
            for k in m.get('Moments'):
                temp_model = ListMomentsResponseBodyMoments()
                self.moments.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListMomentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMomentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMomentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPhotoFacesRequest(TeaModel):
    def __init__(
        self,
        photo_id: int = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.photo_id = photo_id
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class ListPhotoFacesResponseBodyFaces(TeaModel):
    def __init__(
        self,
        face_id_str: str = None,
        face_name: str = None,
        face_id: int = None,
        axis: List[str] = None,
    ):
        self.face_id_str = face_id_str
        self.face_name = face_name
        self.face_id = face_id
        self.axis = axis

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_id_str is not None:
            result['FaceIdStr'] = self.face_id_str
        if self.face_name is not None:
            result['FaceName'] = self.face_name
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.axis is not None:
            result['Axis'] = self.axis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceIdStr') is not None:
            self.face_id_str = m.get('FaceIdStr')
        if m.get('FaceName') is not None:
            self.face_name = m.get('FaceName')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('Axis') is not None:
            self.axis = m.get('Axis')
        return self


class ListPhotoFacesResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
        faces: List[ListPhotoFacesResponseBodyFaces] = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code
        self.faces = faces

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = ListPhotoFacesResponseBodyFaces()
                self.faces.append(temp_model.from_map(k))
        return self


class ListPhotoFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPhotoFacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPhotoFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPhotosRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        size: int = None,
        cursor: str = None,
        state: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.direction = direction
        self.size = size
        self.cursor = cursor
        self.state = state
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.size is not None:
            result['Size'] = self.size
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.state is not None:
            result['State'] = self.state
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class ListPhotosResponseBodyPhotos(TeaModel):
    def __init__(
        self,
        remark: str = None,
        taken_at: int = None,
        state: str = None,
        height: int = None,
        share_expire_time: int = None,
        file_id: str = None,
        id_str: str = None,
        ctime: int = None,
        mtime: int = None,
        size: int = None,
        width: int = None,
        inactive_time: int = None,
        md_5: str = None,
        is_video: bool = None,
        title: str = None,
        location: str = None,
        id: int = None,
    ):
        self.remark = remark
        self.taken_at = taken_at
        self.state = state
        self.height = height
        self.share_expire_time = share_expire_time
        self.file_id = file_id
        self.id_str = id_str
        self.ctime = ctime
        self.mtime = mtime
        self.size = size
        self.width = width
        self.inactive_time = inactive_time
        self.md_5 = md_5
        self.is_video = is_video
        self.title = title
        self.location = location
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.size is not None:
            result['Size'] = self.size
        if self.width is not None:
            result['Width'] = self.width
        if self.inactive_time is not None:
            result['InactiveTime'] = self.inactive_time
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.title is not None:
            result['Title'] = self.title
        if self.location is not None:
            result['Location'] = self.location
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('InactiveTime') is not None:
            self.inactive_time = m.get('InactiveTime')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListPhotosResponseBody(TeaModel):
    def __init__(
        self,
        photos: List[ListPhotosResponseBodyPhotos] = None,
        action: str = None,
        total_count: int = None,
        next_cursor: str = None,
        request_id: str = None,
        message: str = None,
        code: str = None,
    ):
        self.photos = photos
        self.action = action
        self.total_count = total_count
        self.next_cursor = next_cursor
        self.request_id = request_id
        self.message = message
        self.code = code

    def validate(self):
        if self.photos:
            for k in self.photos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Photos'] = []
        if self.photos is not None:
            for k in self.photos:
                result['Photos'].append(k.to_map() if k else None)
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_cursor is not None:
            result['NextCursor'] = self.next_cursor
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.photos = []
        if m.get('Photos') is not None:
            for k in m.get('Photos'):
                temp_model = ListPhotosResponseBodyPhotos()
                self.photos.append(temp_model.from_map(k))
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextCursor') is not None:
            self.next_cursor = m.get('NextCursor')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPhotoStoresResponseBodyPhotoStoresBuckets(TeaModel):
    def __init__(
        self,
        state: str = None,
        region: str = None,
        name: str = None,
    ):
        self.state = state
        self.region = region
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.region is not None:
            result['Region'] = self.region
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListPhotoStoresResponseBodyPhotoStores(TeaModel):
    def __init__(
        self,
        auto_clean_days: int = None,
        id_str: str = None,
        mtime: int = None,
        ctime: int = None,
        remark: str = None,
        buckets: List[ListPhotoStoresResponseBodyPhotoStoresBuckets] = None,
        default_quota: int = None,
        name: str = None,
        auto_clean_enabled: bool = None,
        id: int = None,
    ):
        self.auto_clean_days = auto_clean_days
        self.id_str = id_str
        self.mtime = mtime
        self.ctime = ctime
        self.remark = remark
        self.buckets = buckets
        self.default_quota = default_quota
        self.name = name
        self.auto_clean_enabled = auto_clean_enabled
        self.id = id

    def validate(self):
        if self.buckets:
            for k in self.buckets:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auto_clean_days is not None:
            result['AutoCleanDays'] = self.auto_clean_days
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.remark is not None:
            result['Remark'] = self.remark
        result['Buckets'] = []
        if self.buckets is not None:
            for k in self.buckets:
                result['Buckets'].append(k.to_map() if k else None)
        if self.default_quota is not None:
            result['DefaultQuota'] = self.default_quota
        if self.name is not None:
            result['Name'] = self.name
        if self.auto_clean_enabled is not None:
            result['AutoCleanEnabled'] = self.auto_clean_enabled
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCleanDays') is not None:
            self.auto_clean_days = m.get('AutoCleanDays')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        self.buckets = []
        if m.get('Buckets') is not None:
            for k in m.get('Buckets'):
                temp_model = ListPhotoStoresResponseBodyPhotoStoresBuckets()
                self.buckets.append(temp_model.from_map(k))
        if m.get('DefaultQuota') is not None:
            self.default_quota = m.get('DefaultQuota')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AutoCleanEnabled') is not None:
            self.auto_clean_enabled = m.get('AutoCleanEnabled')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListPhotoStoresResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        photo_stores: List[ListPhotoStoresResponseBodyPhotoStores] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.photo_stores = photo_stores
        self.code = code

    def validate(self):
        if self.photo_stores:
            for k in self.photo_stores:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PhotoStores'] = []
        if self.photo_stores is not None:
            for k in self.photo_stores:
                result['PhotoStores'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.photo_stores = []
        if m.get('PhotoStores') is not None:
            for k in m.get('PhotoStores'):
                temp_model = ListPhotoStoresResponseBodyPhotoStores()
                self.photo_stores.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListPhotoStoresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPhotoStoresResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPhotoStoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPhotoTagsRequest(TeaModel):
    def __init__(
        self,
        photo_id: int = None,
        store_name: str = None,
        library_id: str = None,
        lang: str = None,
    ):
        self.photo_id = photo_id
        self.store_name = store_name
        self.library_id = library_id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ListPhotoTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        is_sub_tag: bool = None,
        name: str = None,
        parent_tag: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.is_sub_tag = is_sub_tag
        self.name = name
        self.parent_tag = parent_tag
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.is_sub_tag is not None:
            result['IsSubTag'] = self.is_sub_tag
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_tag is not None:
            result['ParentTag'] = self.parent_tag
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('IsSubTag') is not None:
            self.is_sub_tag = m.get('IsSubTag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentTag') is not None:
            self.parent_tag = m.get('ParentTag')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListPhotoTagsResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
        tags: List[ListPhotoTagsResponseBodyTags] = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListPhotoTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListPhotoTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPhotoTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPhotoTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegisteredTagsRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        lang: List[str] = None,
    ):
        self.store_name = store_name
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ListRegisteredTagsResponseBodyRegisteredTagsTagValues(TeaModel):
    def __init__(
        self,
        lang: str = None,
        text: str = None,
    ):
        self.lang = lang
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class ListRegisteredTagsResponseBodyRegisteredTags(TeaModel):
    def __init__(
        self,
        tag_values: List[ListRegisteredTagsResponseBodyRegisteredTagsTagValues] = None,
        tag_key: str = None,
    ):
        self.tag_values = tag_values
        self.tag_key = tag_key

    def validate(self):
        if self.tag_values:
            for k in self.tag_values:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagValues'] = []
        if self.tag_values is not None:
            for k in self.tag_values:
                result['TagValues'].append(k.to_map() if k else None)
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_values = []
        if m.get('TagValues') is not None:
            for k in m.get('TagValues'):
                temp_model = ListRegisteredTagsResponseBodyRegisteredTagsTagValues()
                self.tag_values.append(temp_model.from_map(k))
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListRegisteredTagsResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        registered_tags: List[ListRegisteredTagsResponseBodyRegisteredTags] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.registered_tags = registered_tags
        self.code = code

    def validate(self):
        if self.registered_tags:
            for k in self.registered_tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RegisteredTags'] = []
        if self.registered_tags is not None:
            for k in self.registered_tags:
                result['RegisteredTags'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.registered_tags = []
        if m.get('RegisteredTags') is not None:
            for k in m.get('RegisteredTags'):
                temp_model = ListRegisteredTagsResponseBodyRegisteredTags()
                self.registered_tags.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListRegisteredTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRegisteredTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRegisteredTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagPhotosRequest(TeaModel):
    def __init__(
        self,
        tag_id: int = None,
        direction: str = None,
        size: int = None,
        cursor: str = None,
        state: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.tag_id = tag_id
        self.direction = direction
        self.size = size
        self.cursor = cursor
        self.state = state
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.size is not None:
            result['Size'] = self.size
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.state is not None:
            result['State'] = self.state
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class ListTagPhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        photo_id_str: str = None,
        state: str = None,
        photo_id: int = None,
    ):
        self.photo_id_str = photo_id_str
        self.state = state
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.photo_id_str is not None:
            result['PhotoIdStr'] = self.photo_id_str
        if self.state is not None:
            result['State'] = self.state
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhotoIdStr') is not None:
            self.photo_id_str = m.get('PhotoIdStr')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class ListTagPhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        total_count: int = None,
        next_cursor: str = None,
        request_id: str = None,
        message: str = None,
        results: List[ListTagPhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.total_count = total_count
        self.next_cursor = next_cursor
        self.request_id = request_id
        self.message = message
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_cursor is not None:
            result['NextCursor'] = self.next_cursor
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextCursor') is not None:
            self.next_cursor = m.get('NextCursor')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ListTagPhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListTagPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.lang = lang
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class ListTagsResponseBodyTagsCover(TeaModel):
    def __init__(
        self,
        remark: str = None,
        state: str = None,
        height: int = None,
        file_id: str = None,
        id_str: str = None,
        mtime: int = None,
        ctime: int = None,
        width: int = None,
        md_5: str = None,
        is_video: bool = None,
        title: str = None,
        id: int = None,
    ):
        self.remark = remark
        self.state = state
        self.height = height
        self.file_id = file_id
        self.id_str = id_str
        self.mtime = mtime
        self.ctime = ctime
        self.width = width
        self.md_5 = md_5
        self.is_video = is_video
        self.title = title
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.width is not None:
            result['Width'] = self.width
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.title is not None:
            result['Title'] = self.title
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        cover: ListTagsResponseBodyTagsCover = None,
        is_sub_tag: bool = None,
        name: str = None,
        parent_tag: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.cover = cover
        self.is_sub_tag = is_sub_tag
        self.name = name
        self.parent_tag = parent_tag
        self.id = id

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.is_sub_tag is not None:
            result['IsSubTag'] = self.is_sub_tag
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_tag is not None:
            result['ParentTag'] = self.parent_tag
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Cover') is not None:
            temp_model = ListTagsResponseBodyTagsCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('IsSubTag') is not None:
            self.is_sub_tag = m.get('IsSubTag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentTag') is not None:
            self.parent_tag = m.get('ParentTag')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
        tags: List[ListTagsResponseBodyTags] = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTimeLinePhotosRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        page: int = None,
        size: int = None,
        start_time: int = None,
        end_time: int = None,
        filter_by: str = None,
        order: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.direction = direction
        self.page = page
        self.size = size
        self.start_time = start_time
        self.end_time = end_time
        self.filter_by = filter_by
        self.order = order
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_by is not None:
            result['FilterBy'] = self.filter_by
        if self.order is not None:
            result['Order'] = self.order
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterBy') is not None:
            self.filter_by = m.get('FilterBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class ListTimeLinePhotosResponseBodyPhotos(TeaModel):
    def __init__(
        self,
        remark: str = None,
        taken_at: int = None,
        state: str = None,
        height: int = None,
        share_expire_time: int = None,
        file_id: str = None,
        id_str: str = None,
        ctime: int = None,
        mtime: int = None,
        size: int = None,
        width: int = None,
        md_5: str = None,
        is_video: bool = None,
        title: str = None,
        like: int = None,
        location: str = None,
        id: int = None,
    ):
        self.remark = remark
        self.taken_at = taken_at
        self.state = state
        self.height = height
        self.share_expire_time = share_expire_time
        self.file_id = file_id
        self.id_str = id_str
        self.ctime = ctime
        self.mtime = mtime
        self.size = size
        self.width = width
        self.md_5 = md_5
        self.is_video = is_video
        self.title = title
        self.like = like
        self.location = location
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.size is not None:
            result['Size'] = self.size
        if self.width is not None:
            result['Width'] = self.width
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.title is not None:
            result['Title'] = self.title
        if self.like is not None:
            result['Like'] = self.like
        if self.location is not None:
            result['Location'] = self.location
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Like') is not None:
            self.like = m.get('Like')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListTimeLinePhotosResponseBody(TeaModel):
    def __init__(
        self,
        photos: List[ListTimeLinePhotosResponseBodyPhotos] = None,
        action: str = None,
        total_count: int = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.photos = photos
        self.action = action
        self.total_count = total_count
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.photos:
            for k in self.photos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Photos'] = []
        if self.photos is not None:
            for k in self.photos:
                result['Photos'].append(k.to_map() if k else None)
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.photos = []
        if m.get('Photos') is not None:
            for k in m.get('Photos'):
                temp_model = ListTimeLinePhotosResponseBodyPhotos()
                self.photos.append(temp_model.from_map(k))
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListTimeLinePhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTimeLinePhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTimeLinePhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTimeLinesRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        photo_size: int = None,
        cursor: int = None,
        time_line_count: int = None,
        time_line_unit: str = None,
        filter_by: str = None,
        order: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.direction = direction
        self.photo_size = photo_size
        self.cursor = cursor
        self.time_line_count = time_line_count
        self.time_line_unit = time_line_unit
        self.filter_by = filter_by
        self.order = order
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.photo_size is not None:
            result['PhotoSize'] = self.photo_size
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.time_line_count is not None:
            result['TimeLineCount'] = self.time_line_count
        if self.time_line_unit is not None:
            result['TimeLineUnit'] = self.time_line_unit
        if self.filter_by is not None:
            result['FilterBy'] = self.filter_by
        if self.order is not None:
            result['Order'] = self.order
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('PhotoSize') is not None:
            self.photo_size = m.get('PhotoSize')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('TimeLineCount') is not None:
            self.time_line_count = m.get('TimeLineCount')
        if m.get('TimeLineUnit') is not None:
            self.time_line_unit = m.get('TimeLineUnit')
        if m.get('FilterBy') is not None:
            self.filter_by = m.get('FilterBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class ListTimeLinesResponseBodyTimeLinesPhotos(TeaModel):
    def __init__(
        self,
        remark: str = None,
        taken_at: int = None,
        state: str = None,
        height: int = None,
        share_expire_time: int = None,
        file_id: str = None,
        id_str: str = None,
        ctime: int = None,
        mtime: int = None,
        size: int = None,
        width: int = None,
        md_5: str = None,
        is_video: bool = None,
        title: str = None,
        like: int = None,
        location: str = None,
        id: int = None,
    ):
        self.remark = remark
        self.taken_at = taken_at
        self.state = state
        self.height = height
        self.share_expire_time = share_expire_time
        self.file_id = file_id
        self.id_str = id_str
        self.ctime = ctime
        self.mtime = mtime
        self.size = size
        self.width = width
        self.md_5 = md_5
        self.is_video = is_video
        self.title = title
        self.like = like
        self.location = location
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.size is not None:
            result['Size'] = self.size
        if self.width is not None:
            result['Width'] = self.width
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.title is not None:
            result['Title'] = self.title
        if self.like is not None:
            result['Like'] = self.like
        if self.location is not None:
            result['Location'] = self.location
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Like') is not None:
            self.like = m.get('Like')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListTimeLinesResponseBodyTimeLines(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        photos_count: int = None,
        start_time: int = None,
        photos: List[ListTimeLinesResponseBodyTimeLinesPhotos] = None,
        total_count: int = None,
    ):
        self.end_time = end_time
        self.photos_count = photos_count
        self.start_time = start_time
        self.photos = photos
        self.total_count = total_count

    def validate(self):
        if self.photos:
            for k in self.photos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.photos_count is not None:
            result['PhotosCount'] = self.photos_count
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Photos'] = []
        if self.photos is not None:
            for k in self.photos:
                result['Photos'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PhotosCount') is not None:
            self.photos_count = m.get('PhotosCount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.photos = []
        if m.get('Photos') is not None:
            for k in m.get('Photos'):
                temp_model = ListTimeLinesResponseBodyTimeLinesPhotos()
                self.photos.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTimeLinesResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        next_cursor: int = None,
        time_lines: List[ListTimeLinesResponseBodyTimeLines] = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.next_cursor = next_cursor
        self.time_lines = time_lines
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.time_lines:
            for k in self.time_lines:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.next_cursor is not None:
            result['NextCursor'] = self.next_cursor
        result['TimeLines'] = []
        if self.time_lines is not None:
            for k in self.time_lines:
                result['TimeLines'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('NextCursor') is not None:
            self.next_cursor = m.get('NextCursor')
        self.time_lines = []
        if m.get('TimeLines') is not None:
            for k in m.get('TimeLines'):
                temp_model = ListTimeLinesResponseBodyTimeLines()
                self.time_lines.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListTimeLinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTimeLinesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTimeLinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MergeFacesRequest(TeaModel):
    def __init__(
        self,
        target_face_id: int = None,
        store_name: str = None,
        library_id: str = None,
        face_id: List[int] = None,
    ):
        self.target_face_id = target_face_id
        self.store_name = store_name
        self.library_id = library_id
        self.face_id = face_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.target_face_id is not None:
            result['TargetFaceId'] = self.target_face_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetFaceId') is not None:
            self.target_face_id = m.get('TargetFaceId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        return self


class MergeFacesResponseBodyResultsResult(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MergeFacesResponseBodyResults(TeaModel):
    def __init__(
        self,
        result: List[MergeFacesResponseBodyResultsResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = MergeFacesResponseBodyResultsResult()
                self.result.append(temp_model.from_map(k))
        return self


class MergeFacesResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: MergeFacesResponseBodyResults = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.results is not None:
            result['Results'] = self.results.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Results') is not None:
            temp_model = MergeFacesResponseBodyResults()
            self.results = temp_model.from_map(m['Results'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class MergeFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MergeFacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MergeFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveAlbumPhotosRequest(TeaModel):
    def __init__(
        self,
        source_album_id: int = None,
        target_album_id: int = None,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.source_album_id = source_album_id
        self.target_album_id = target_album_id
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_album_id is not None:
            result['SourceAlbumId'] = self.source_album_id
        if self.target_album_id is not None:
            result['TargetAlbumId'] = self.target_album_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceAlbumId') is not None:
            self.source_album_id = m.get('SourceAlbumId')
        if m.get('TargetAlbumId') is not None:
            self.target_album_id = m.get('TargetAlbumId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class MoveAlbumPhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MoveAlbumPhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[MoveAlbumPhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = MoveAlbumPhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class MoveAlbumPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveAlbumPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MoveAlbumPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveFacePhotosRequest(TeaModel):
    def __init__(
        self,
        source_face_id: int = None,
        target_face_id: int = None,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.source_face_id = source_face_id
        self.target_face_id = target_face_id
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_face_id is not None:
            result['SourceFaceId'] = self.source_face_id
        if self.target_face_id is not None:
            result['TargetFaceId'] = self.target_face_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceFaceId') is not None:
            self.source_face_id = m.get('SourceFaceId')
        if m.get('TargetFaceId') is not None:
            self.target_face_id = m.get('TargetFaceId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class MoveFacePhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MoveFacePhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[MoveFacePhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = MoveFacePhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class MoveFacePhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveFacePhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MoveFacePhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReactivatePhotosRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class ReactivatePhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ReactivatePhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[ReactivatePhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ReactivatePhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ReactivatePhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReactivatePhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReactivatePhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterPhotoRequest(TeaModel):
    def __init__(
        self,
        taken_at: int = None,
        location: str = None,
        store_name: str = None,
        library_id: str = None,
        latitude: float = None,
        longitude: float = None,
        width: int = None,
        height: int = None,
        is_video: str = None,
        md_5: str = None,
        size: int = None,
        photo_title: str = None,
        remark: str = None,
    ):
        self.taken_at = taken_at
        self.location = location
        self.store_name = store_name
        self.library_id = library_id
        self.latitude = latitude
        self.longitude = longitude
        self.width = width
        self.height = height
        self.is_video = is_video
        self.md_5 = md_5
        self.size = size
        self.photo_title = photo_title
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.location is not None:
            result['Location'] = self.location
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.size is not None:
            result['Size'] = self.size
        if self.photo_title is not None:
            result['PhotoTitle'] = self.photo_title
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('PhotoTitle') is not None:
            self.photo_title = m.get('PhotoTitle')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class RegisterPhotoResponseBodyPhoto(TeaModel):
    def __init__(
        self,
        remark: str = None,
        taken_at: int = None,
        state: str = None,
        height: int = None,
        share_expire_time: int = None,
        file_id: str = None,
        id_str: str = None,
        ctime: int = None,
        mtime: int = None,
        width: int = None,
        size: int = None,
        md_5: str = None,
        title: str = None,
        is_video: bool = None,
        id: int = None,
        location: str = None,
    ):
        self.remark = remark
        self.taken_at = taken_at
        self.state = state
        self.height = height
        self.share_expire_time = share_expire_time
        self.file_id = file_id
        self.id_str = id_str
        self.ctime = ctime
        self.mtime = mtime
        self.width = width
        self.size = size
        self.md_5 = md_5
        self.title = title
        self.is_video = is_video
        self.id = id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.width is not None:
            result['Width'] = self.width
        if self.size is not None:
            result['Size'] = self.size
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.title is not None:
            result['Title'] = self.title
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class RegisterPhotoResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        photo: RegisterPhotoResponseBodyPhoto = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.photo = photo
        self.code = code

    def validate(self):
        if self.photo:
            self.photo.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.photo is not None:
            result['Photo'] = self.photo.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Photo') is not None:
            temp_model = RegisterPhotoResponseBodyPhoto()
            self.photo = temp_model.from_map(m['Photo'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RegisterPhotoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterPhotoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RegisterPhotoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterTagRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        tag_key: str = None,
        lang: str = None,
        text: str = None,
    ):
        self.store_name = store_name
        self.tag_key = tag_key
        self.lang = lang
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RegisterTagResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RegisterTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterTagResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RegisterTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAlbumPhotosRequest(TeaModel):
    def __init__(
        self,
        album_id: int = None,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.album_id = album_id
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class RemoveAlbumPhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class RemoveAlbumPhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[RemoveAlbumPhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RemoveAlbumPhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RemoveAlbumPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveAlbumPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveAlbumPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFacePhotosRequest(TeaModel):
    def __init__(
        self,
        face_id: int = None,
        store_name: str = None,
        library_id: str = None,
        photo_id: List[int] = None,
    ):
        self.face_id = face_id
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        return self


class RemoveFacePhotosResponseBodyResults(TeaModel):
    def __init__(
        self,
        id_str: str = None,
        code: str = None,
        message: str = None,
        id: int = None,
    ):
        self.id_str = id_str
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class RemoveFacePhotosResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        results: List[RemoveFacePhotosResponseBodyResults] = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.results = results
        self.code = code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RemoveFacePhotosResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RemoveFacePhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveFacePhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveFacePhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameAlbumRequest(TeaModel):
    def __init__(
        self,
        album_id: int = None,
        album_name: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.album_id = album_id
        self.album_name = album_name
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class RenameAlbumResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RenameAlbumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenameAlbumResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenameAlbumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameFaceRequest(TeaModel):
    def __init__(
        self,
        face_id: int = None,
        face_name: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.face_id = face_id
        self.face_name = face_name
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.face_name is not None:
            result['FaceName'] = self.face_name
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('FaceName') is not None:
            self.face_name = m.get('FaceName')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class RenameFaceResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RenameFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenameFaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenameFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchPhotosRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        keyword: str = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.page = page
        self.size = size
        self.keyword = keyword
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class SearchPhotosResponseBodyPhotos(TeaModel):
    def __init__(
        self,
        taken_at: int = None,
        state: str = None,
        height: int = None,
        share_expire_time: int = None,
        file_id: str = None,
        id_str: str = None,
        ctime: int = None,
        mtime: int = None,
        width: int = None,
        size: int = None,
        md_5: str = None,
        title: str = None,
        is_video: bool = None,
        id: int = None,
        location: str = None,
    ):
        self.taken_at = taken_at
        self.state = state
        self.height = height
        self.share_expire_time = share_expire_time
        self.file_id = file_id
        self.id_str = id_str
        self.ctime = ctime
        self.mtime = mtime
        self.width = width
        self.size = size
        self.md_5 = md_5
        self.title = title
        self.is_video = is_video
        self.id = id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.taken_at is not None:
            result['TakenAt'] = self.taken_at
        if self.state is not None:
            result['State'] = self.state
        if self.height is not None:
            result['Height'] = self.height
        if self.share_expire_time is not None:
            result['ShareExpireTime'] = self.share_expire_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id_str is not None:
            result['IdStr'] = self.id_str
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.width is not None:
            result['Width'] = self.width
        if self.size is not None:
            result['Size'] = self.size
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.title is not None:
            result['Title'] = self.title
        if self.is_video is not None:
            result['IsVideo'] = self.is_video
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TakenAt') is not None:
            self.taken_at = m.get('TakenAt')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ShareExpireTime') is not None:
            self.share_expire_time = m.get('ShareExpireTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IdStr') is not None:
            self.id_str = m.get('IdStr')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('IsVideo') is not None:
            self.is_video = m.get('IsVideo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class SearchPhotosResponseBody(TeaModel):
    def __init__(
        self,
        photos: List[SearchPhotosResponseBodyPhotos] = None,
        action: str = None,
        total_count: int = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.photos = photos
        self.action = action
        self.total_count = total_count
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.photos:
            for k in self.photos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Photos'] = []
        if self.photos is not None:
            for k in self.photos:
                result['Photos'].append(k.to_map() if k else None)
        if self.action is not None:
            result['Action'] = self.action
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.photos = []
        if m.get('Photos') is not None:
            for k in m.get('Photos'):
                temp_model = SearchPhotosResponseBodyPhotos()
                self.photos.append(temp_model.from_map(k))
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SearchPhotosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchPhotosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchPhotosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAlbumCoverRequest(TeaModel):
    def __init__(
        self,
        album_id: int = None,
        photo_id: int = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.album_id = album_id
        self.photo_id = photo_id
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class SetAlbumCoverResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SetAlbumCoverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetAlbumCoverResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetAlbumCoverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFaceCoverRequest(TeaModel):
    def __init__(
        self,
        face_id: int = None,
        photo_id: int = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.face_id = face_id
        self.photo_id = photo_id
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class SetFaceCoverResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SetFaceCoverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetFaceCoverResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetFaceCoverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMeRequest(TeaModel):
    def __init__(
        self,
        face_id: int = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.face_id = face_id
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class SetMeResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SetMeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetMeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetMeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetQuotaRequest(TeaModel):
    def __init__(
        self,
        total_quota: int = None,
        store_name: str = None,
        library_id: str = None,
    ):
        self.total_quota = total_quota
        self.store_name = store_name
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        return self


class SetQuotaResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SetQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetQuotaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagPhotoRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        library_id: str = None,
        photo_id: int = None,
        tag_key: List[str] = None,
        confidence: List[int] = None,
    ):
        self.store_name = store_name
        self.library_id = library_id
        self.photo_id = photo_id
        self.tag_key = tag_key
        self.confidence = confidence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.library_id is not None:
            result['LibraryId'] = self.library_id
        if self.photo_id is not None:
            result['PhotoId'] = self.photo_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('LibraryId') is not None:
            self.library_id = m.get('LibraryId')
        if m.get('PhotoId') is not None:
            self.photo_id = m.get('PhotoId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class TagPhotoResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class TagPhotoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagPhotoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagPhotoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ToggleFeaturesRequest(TeaModel):
    def __init__(
        self,
        store_name: str = None,
        enabled_features: List[str] = None,
        disabled_features: List[str] = None,
    ):
        self.store_name = store_name
        self.enabled_features = enabled_features
        self.disabled_features = disabled_features

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.enabled_features is not None:
            result['EnabledFeatures'] = self.enabled_features
        if self.disabled_features is not None:
            result['DisabledFeatures'] = self.disabled_features
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('EnabledFeatures') is not None:
            self.enabled_features = m.get('EnabledFeatures')
        if m.get('DisabledFeatures') is not None:
            self.disabled_features = m.get('DisabledFeatures')
        return self


class ToggleFeaturesResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.action = action
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ToggleFeaturesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ToggleFeaturesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ToggleFeaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


