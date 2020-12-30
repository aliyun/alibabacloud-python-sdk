# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class AddFacesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class AddFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class AddGroupsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class AddGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class AddPersonRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class AddPersonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class AddSimilarityImageRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class AddSimilarityImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class AddSimilarityLibraryRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class AddSimilarityLibraryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class AddVideoDnaRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class AddVideoDnaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class AddVideoDnaGroupRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class AddVideoDnaGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteFacesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class DeleteFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteGroupsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class DeleteGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeletePersonRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class DeletePersonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteSimilarityImageRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class DeleteSimilarityImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteSimilarityLibraryRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class DeleteSimilarityLibraryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteVideoDnaRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class DeleteVideoDnaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteVideoDnaGroupRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class DeleteVideoDnaGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DetectFaceRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class DetectFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class FileAsyncScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class FileAsyncScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class FileAsyncScanResultsRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class FileAsyncScanResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetAddVideoDnaResultsRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class GetAddVideoDnaResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetFacesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class GetFacesResponseBody(TeaModel):
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


class GetFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFacesResponseBody = None,
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
            temp_model = GetFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class GetGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetPersonRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class GetPersonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetPersonsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class GetPersonsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetSimilarityImageRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class GetSimilarityImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetSimilarityLibraryRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class GetSimilarityLibraryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ImageAsyncManualScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class ImageAsyncManualScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ImageAsyncManualScanResultsRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class ImageAsyncManualScanResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ImageAsyncScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class ImageAsyncScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ImageAsyncScanResultsRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class ImageAsyncScanResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ImageScanFeedbackRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class ImageScanFeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ImageSyncScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class ImageSyncScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ListSimilarityImagesRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class ListSimilarityImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ListSimilarityLibrariesRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class ListSimilarityLibrariesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class LiveStreamAsyncScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class LiveStreamAsyncScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class LiveStreamAsyncScanResultsRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class LiveStreamAsyncScanResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class LiveStreamCancelScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class LiveStreamCancelScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class SearchPersonRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class SearchPersonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class SetPersonRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class SetPersonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class TextAsyncManualScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class TextAsyncManualScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class TextAsyncManualScanResultsRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class TextAsyncManualScanResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class TextFeedbackRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class TextFeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class TextScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class TextScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UploadCredentialsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class UploadCredentialsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VideoAsyncManualScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VideoAsyncManualScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VideoAsyncManualScanResultsRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VideoAsyncManualScanResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VideoAsyncScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VideoAsyncScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VideoAsyncScanResultsRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VideoAsyncScanResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VideoCancelScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VideoCancelScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VideoFeedbackRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VideoFeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VideoSyncScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VideoSyncScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VodAsyncScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VodAsyncScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VodAsyncScanResultsRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VodAsyncScanResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VoiceAsyncManualScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VoiceAsyncManualScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VoiceAsyncManualScanResultsRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VoiceAsyncManualScanResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VoiceAsyncScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VoiceAsyncScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VoiceAsyncScanResultsRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VoiceAsyncScanResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VoiceCancelScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VoiceCancelScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VoiceIdentityCheckRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VoiceIdentityCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VoiceIdentityRegisterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VoiceIdentityRegisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VoiceIdentityStartCheckRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VoiceIdentityStartCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VoiceIdentityStartRegisterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VoiceIdentityStartRegisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VoiceIdentityUnregisterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VoiceIdentityUnregisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class VoiceSyncScanRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_info: str = None,
    ):
        self.region_id = region_id
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class VoiceSyncScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class WebpageAsyncScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class WebpageAsyncScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class WebpageAsyncScanResultsRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class WebpageAsyncScanResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class WebpageSyncScanRequest(TeaModel):
    def __init__(
        self,
        client_info: str = None,
    ):
        self.client_info = client_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        return self


class WebpageSyncScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


