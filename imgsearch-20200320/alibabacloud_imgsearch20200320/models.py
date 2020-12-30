# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, List


class AddImageRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        image_url: str = None,
        extra_data: str = None,
        entity_id: str = None,
    ):
        self.db_name = db_name
        self.image_url = image_url
        self.extra_data = extra_data
        self.entity_id = entity_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        return self


class AddImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_url_object: BinaryIO = None,
        db_name: str = None,
        extra_data: str = None,
        entity_id: str = None,
    ):
        self.image_url_object = image_url_object
        self.db_name = db_name
        self.extra_data = extra_data
        self.entity_id = entity_id

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')

    def to_map(self):
        result = dict()
        if self.image_url_object is not None:
            result['ImageUrlObject'] = self.image_url_object
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrlObject') is not None:
            self.image_url_object = m.get('ImageUrlObject')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        return self


class AddImageResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
    ):
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class AddImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AddImageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AddImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddImageResponseBody = None,
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
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageDbRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateImageDbResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageDbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateImageDbResponseBody = None,
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
            temp_model = CreateImageDbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        entity_id: str = None,
    ):
        self.db_name = db_name
        self.entity_id = entity_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteImageResponseBody = None,
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
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageDbRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteImageDbResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImageDbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteImageDbResponseBody = None,
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
            temp_model = DeleteImageDbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImageDbsResponseBodyDataDbList(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListImageDbsResponseBodyData(TeaModel):
    def __init__(
        self,
        db_list: List[ListImageDbsResponseBodyDataDbList] = None,
    ):
        self.db_list = db_list

    def validate(self):
        if self.db_list:
            for k in self.db_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DbList'] = []
        if self.db_list is not None:
            for k in self.db_list:
                result['DbList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.db_list = []
        if m.get('DbList') is not None:
            for k in m.get('DbList'):
                temp_model = ListImageDbsResponseBodyDataDbList()
                self.db_list.append(temp_model.from_map(k))
        return self


class ListImageDbsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListImageDbsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListImageDbsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListImageDbsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListImageDbsResponseBody = None,
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
            temp_model = ListImageDbsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        token: str = None,
        offset: int = None,
        limit: int = None,
        order: str = None,
        entity_id_prefix: str = None,
    ):
        self.db_name = db_name
        self.token = token
        self.offset = offset
        self.limit = limit
        self.order = order
        self.entity_id_prefix = entity_id_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.token is not None:
            result['Token'] = self.token
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order is not None:
            result['Order'] = self.order
        if self.entity_id_prefix is not None:
            result['EntityIdPrefix'] = self.entity_id_prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('EntityIdPrefix') is not None:
            self.entity_id_prefix = m.get('EntityIdPrefix')
        return self


class ListImagesResponseBodyDataImageList(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        created_at: int = None,
        updated_at: int = None,
        data_id: str = None,
        extra_data: str = None,
    ):
        self.entity_id = entity_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.data_id = data_id
        self.extra_data = extra_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        return self


class ListImagesResponseBodyData(TeaModel):
    def __init__(
        self,
        image_list: List[ListImagesResponseBodyDataImageList] = None,
        token: str = None,
        total_count: int = None,
    ):
        self.image_list = image_list
        self.token = token
        self.total_count = total_count

    def validate(self):
        if self.image_list:
            for k in self.image_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ImageList'] = []
        if self.image_list is not None:
            for k in self.image_list:
                result['ImageList'].append(k.to_map() if k else None)
        if self.token is not None:
            result['Token'] = self.token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_list = []
        if m.get('ImageList') is not None:
            for k in m.get('ImageList'):
                temp_model = ListImagesResponseBodyDataImageList()
                self.image_list.append(temp_model.from_map(k))
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListImagesResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListImagesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListImagesResponseBody = None,
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
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        image_url: str = None,
        limit: int = None,
    ):
        self.db_name = db_name
        self.image_url = image_url
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class SearchImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_url_object: BinaryIO = None,
        db_name: str = None,
        limit: int = None,
    ):
        self.image_url_object = image_url_object
        self.db_name = db_name
        self.limit = limit

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')

    def to_map(self):
        result = dict()
        if self.image_url_object is not None:
            result['ImageUrlObject'] = self.image_url_object
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrlObject') is not None:
            self.image_url_object = m.get('ImageUrlObject')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class SearchImageResponseBodyDataMatchList(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        entity_id: str = None,
        score: float = None,
        data_id: str = None,
        extra_data: str = None,
    ):
        self.image_url = image_url
        self.entity_id = entity_id
        self.score = score
        self.data_id = data_id
        self.extra_data = extra_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.score is not None:
            result['Score'] = self.score
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        return self


class SearchImageResponseBodyData(TeaModel):
    def __init__(
        self,
        match_list: List[SearchImageResponseBodyDataMatchList] = None,
    ):
        self.match_list = match_list

    def validate(self):
        if self.match_list:
            for k in self.match_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['MatchList'] = []
        if self.match_list is not None:
            for k in self.match_list:
                result['MatchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.match_list = []
        if m.get('MatchList') is not None:
            for k in m.get('MatchList'):
                temp_model = SearchImageResponseBodyDataMatchList()
                self.match_list.append(temp_model.from_map(k))
        return self


class SearchImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SearchImageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SearchImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SearchImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchImageResponseBody = None,
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
            temp_model = SearchImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


