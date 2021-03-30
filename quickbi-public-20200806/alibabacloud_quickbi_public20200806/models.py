# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class QueryDatasetDetailInfoRequest(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
    ):
        self.dataset_id = dataset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        return self


class QueryDatasetDetailInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.success = success
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
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class QueryDatasetDetailInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDatasetDetailInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDatasetDetailInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetListRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
        directory_id: str = None,
        with_children: bool = None,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.workspace_id = workspace_id
        self.directory_id = directory_id
        self.with_children = with_children
        self.keyword = keyword
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.with_children is not None:
            result['WithChildren'] = self.with_children
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('WithChildren') is not None:
            self.with_children = m.get('WithChildren')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryDatasetListResponseBodyResultDataDataSource(TeaModel):
    def __init__(
        self,
        ds_name: str = None,
        ds_id: str = None,
        ds_type: str = None,
    ):
        self.ds_name = ds_name
        self.ds_id = ds_id
        self.ds_type = ds_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ds_name is not None:
            result['DsName'] = self.ds_name
        if self.ds_id is not None:
            result['DsId'] = self.ds_id
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DsName') is not None:
            self.ds_name = m.get('DsName')
        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        return self


class QueryDatasetListResponseBodyResultDataDirectory(TeaModel):
    def __init__(
        self,
        path_name: str = None,
        path_id: str = None,
        name: str = None,
        id: str = None,
    ):
        self.path_name = path_name
        self.path_id = path_id
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path_name is not None:
            result['PathName'] = self.path_name
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QueryDatasetListResponseBodyResultData(TeaModel):
    def __init__(
        self,
        data_source: QueryDatasetListResponseBodyResultDataDataSource = None,
        create_time: str = None,
        owner_name: str = None,
        workspace_name: str = None,
        owner_id: str = None,
        dataset_name: str = None,
        row_level: bool = None,
        workspace_id: str = None,
        description: str = None,
        directory: QueryDatasetListResponseBodyResultDataDirectory = None,
        modify_time: str = None,
        dataset_id: str = None,
    ):
        self.data_source = data_source
        self.create_time = create_time
        self.owner_name = owner_name
        self.workspace_name = workspace_name
        self.owner_id = owner_id
        self.dataset_name = dataset_name
        self.row_level = row_level
        self.workspace_id = workspace_id
        self.description = description
        self.directory = directory
        self.modify_time = modify_time
        self.dataset_id = dataset_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.row_level is not None:
            result['RowLevel'] = self.row_level
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSource') is not None:
            temp_model = QueryDatasetListResponseBodyResultDataDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('RowLevel') is not None:
            self.row_level = m.get('RowLevel')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QueryDatasetListResponseBodyResultDataDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        return self


class QueryDatasetListResponseBodyResult(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        data: List[QueryDatasetListResponseBodyResultData] = None,
        total_pages: int = None,
        page_size: int = None,
        total_num: int = None,
    ):
        self.page_num = page_num
        self.data = data
        self.total_pages = total_pages
        self.page_size = page_size
        self.total_num = total_num

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryDatasetListResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class QueryDatasetListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        result: QueryDatasetListResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.success = success
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
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = QueryDatasetListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class QueryDatasetListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDatasetListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDatasetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


