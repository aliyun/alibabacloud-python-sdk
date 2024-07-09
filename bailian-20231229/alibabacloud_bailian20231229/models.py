# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AddFileRequest(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        lease_id: str = None,
        parser: str = None,
    ):
        # This parameter is required.
        self.category_id = category_id
        # This parameter is required.
        self.lease_id = lease_id
        # This parameter is required.
        self.parser = parser

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.lease_id is not None:
            result['LeaseId'] = self.lease_id
        if self.parser is not None:
            result['Parser'] = self.parser
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('LeaseId') is not None:
            self.lease_id = m.get('LeaseId')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        return self


class AddFileResponseBodyData(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        parser: str = None,
    ):
        self.file_id = file_id
        self.parser = parser

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.parser is not None:
            result['Parser'] = self.parser
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        return self


class AddFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddFileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AddFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFileResponseBody = None,
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
            temp_model = AddFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyFileUploadLeaseRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        md_5: str = None,
        size_in_bytes: str = None,
    ):
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.md_5 = md_5
        # This parameter is required.
        self.size_in_bytes = size_in_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.size_in_bytes is not None:
            result['SizeInBytes'] = self.size_in_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('SizeInBytes') is not None:
            self.size_in_bytes = m.get('SizeInBytes')
        return self


class ApplyFileUploadLeaseResponseBodyDataParam(TeaModel):
    def __init__(
        self,
        headers: Any = None,
        method: str = None,
        url: str = None,
    ):
        self.headers = headers
        self.method = method
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.method is not None:
            result['Method'] = self.method
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ApplyFileUploadLeaseResponseBodyData(TeaModel):
    def __init__(
        self,
        file_upload_lease_id: str = None,
        param: ApplyFileUploadLeaseResponseBodyDataParam = None,
        type: str = None,
    ):
        self.file_upload_lease_id = file_upload_lease_id
        self.param = param
        self.type = type

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_upload_lease_id is not None:
            result['FileUploadLeaseId'] = self.file_upload_lease_id
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUploadLeaseId') is not None:
            self.file_upload_lease_id = m.get('FileUploadLeaseId')
        if m.get('Param') is not None:
            temp_model = ApplyFileUploadLeaseResponseBodyDataParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ApplyFileUploadLeaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ApplyFileUploadLeaseResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ApplyFileUploadLeaseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ApplyFileUploadLeaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyFileUploadLeaseResponseBody = None,
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
            temp_model = ApplyFileUploadLeaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIndexRequestColumns(TeaModel):
    def __init__(
        self,
        column: str = None,
        is_recall: bool = None,
        is_search: bool = None,
        name: str = None,
        type: str = None,
    ):
        self.column = column
        self.is_recall = is_recall
        self.is_search = is_search
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column is not None:
            result['Column'] = self.column
        if self.is_recall is not None:
            result['IsRecall'] = self.is_recall
        if self.is_search is not None:
            result['IsSearch'] = self.is_search
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('IsRecall') is not None:
            self.is_recall = m.get('IsRecall')
        if m.get('IsSearch') is not None:
            self.is_search = m.get('IsSearch')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateIndexRequest(TeaModel):
    def __init__(
        self,
        category_ids: List[str] = None,
        chunk_size: int = None,
        columns: List[CreateIndexRequestColumns] = None,
        description: str = None,
        document_ids: List[str] = None,
        embedding_model_name: str = None,
        name: str = None,
        overlap_size: int = None,
        rerank_min_score: float = None,
        rerank_model_name: str = None,
        separator: str = None,
        sink_instance_id: str = None,
        sink_region: str = None,
        sink_type: str = None,
        source_type: str = None,
        structure_type: str = None,
    ):
        self.category_ids = category_ids
        self.chunk_size = chunk_size
        self.columns = columns
        self.description = description
        self.document_ids = document_ids
        self.embedding_model_name = embedding_model_name
        # This parameter is required.
        self.name = name
        self.overlap_size = overlap_size
        self.rerank_min_score = rerank_min_score
        self.rerank_model_name = rerank_model_name
        self.separator = separator
        self.sink_instance_id = sink_instance_id
        self.sink_region = sink_region
        # This parameter is required.
        self.sink_type = sink_type
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required.
        self.structure_type = structure_type

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.document_ids is not None:
            result['DocumentIds'] = self.document_ids
        if self.embedding_model_name is not None:
            result['EmbeddingModelName'] = self.embedding_model_name
        if self.name is not None:
            result['Name'] = self.name
        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size
        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score
        if self.rerank_model_name is not None:
            result['RerankModelName'] = self.rerank_model_name
        if self.separator is not None:
            result['Separator'] = self.separator
        if self.sink_instance_id is not None:
            result['SinkInstanceId'] = self.sink_instance_id
        if self.sink_region is not None:
            result['SinkRegion'] = self.sink_region
        if self.sink_type is not None:
            result['SinkType'] = self.sink_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.structure_type is not None:
            result['StructureType'] = self.structure_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = CreateIndexRequestColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentIds') is not None:
            self.document_ids = m.get('DocumentIds')
        if m.get('EmbeddingModelName') is not None:
            self.embedding_model_name = m.get('EmbeddingModelName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')
        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')
        if m.get('RerankModelName') is not None:
            self.rerank_model_name = m.get('RerankModelName')
        if m.get('Separator') is not None:
            self.separator = m.get('Separator')
        if m.get('SinkInstanceId') is not None:
            self.sink_instance_id = m.get('SinkInstanceId')
        if m.get('SinkRegion') is not None:
            self.sink_region = m.get('SinkRegion')
        if m.get('SinkType') is not None:
            self.sink_type = m.get('SinkType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StructureType') is not None:
            self.structure_type = m.get('StructureType')
        return self


class CreateIndexShrinkRequest(TeaModel):
    def __init__(
        self,
        category_ids_shrink: str = None,
        chunk_size: int = None,
        columns_shrink: str = None,
        description: str = None,
        document_ids_shrink: str = None,
        embedding_model_name: str = None,
        name: str = None,
        overlap_size: int = None,
        rerank_min_score: float = None,
        rerank_model_name: str = None,
        separator: str = None,
        sink_instance_id: str = None,
        sink_region: str = None,
        sink_type: str = None,
        source_type: str = None,
        structure_type: str = None,
    ):
        self.category_ids_shrink = category_ids_shrink
        self.chunk_size = chunk_size
        self.columns_shrink = columns_shrink
        self.description = description
        self.document_ids_shrink = document_ids_shrink
        self.embedding_model_name = embedding_model_name
        # This parameter is required.
        self.name = name
        self.overlap_size = overlap_size
        self.rerank_min_score = rerank_min_score
        self.rerank_model_name = rerank_model_name
        self.separator = separator
        self.sink_instance_id = sink_instance_id
        self.sink_region = sink_region
        # This parameter is required.
        self.sink_type = sink_type
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required.
        self.structure_type = structure_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink
        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size
        if self.columns_shrink is not None:
            result['Columns'] = self.columns_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.document_ids_shrink is not None:
            result['DocumentIds'] = self.document_ids_shrink
        if self.embedding_model_name is not None:
            result['EmbeddingModelName'] = self.embedding_model_name
        if self.name is not None:
            result['Name'] = self.name
        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size
        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score
        if self.rerank_model_name is not None:
            result['RerankModelName'] = self.rerank_model_name
        if self.separator is not None:
            result['Separator'] = self.separator
        if self.sink_instance_id is not None:
            result['SinkInstanceId'] = self.sink_instance_id
        if self.sink_region is not None:
            result['SinkRegion'] = self.sink_region
        if self.sink_type is not None:
            result['SinkType'] = self.sink_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.structure_type is not None:
            result['StructureType'] = self.structure_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryIds') is not None:
            self.category_ids_shrink = m.get('CategoryIds')
        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')
        if m.get('Columns') is not None:
            self.columns_shrink = m.get('Columns')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentIds') is not None:
            self.document_ids_shrink = m.get('DocumentIds')
        if m.get('EmbeddingModelName') is not None:
            self.embedding_model_name = m.get('EmbeddingModelName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')
        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')
        if m.get('RerankModelName') is not None:
            self.rerank_model_name = m.get('RerankModelName')
        if m.get('Separator') is not None:
            self.separator = m.get('Separator')
        if m.get('SinkInstanceId') is not None:
            self.sink_instance_id = m.get('SinkInstanceId')
        if m.get('SinkRegion') is not None:
            self.sink_region = m.get('SinkRegion')
        if m.get('SinkType') is not None:
            self.sink_type = m.get('SinkType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StructureType') is not None:
            self.structure_type = m.get('StructureType')
        return self


class CreateIndexResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateIndexResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateIndexResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateIndexResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIndexResponseBody = None,
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
            temp_model = CreateIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileResponseBodyData(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        create_time: str = None,
        file_id: str = None,
        file_name: str = None,
        file_type: str = None,
        parser: str = None,
        size_in_bytes: int = None,
        status: str = None,
    ):
        self.category_id = category_id
        self.create_time = create_time
        self.file_id = file_id
        self.file_name = file_name
        self.file_type = file_type
        self.parser = parser
        self.size_in_bytes = size_in_bytes
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.parser is not None:
            result['Parser'] = self.parser
        if self.size_in_bytes is not None:
            result['SizeInBytes'] = self.size_in_bytes
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        if m.get('SizeInBytes') is not None:
            self.size_in_bytes = m.get('SizeInBytes')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeFileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFileResponseBody = None,
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
            temp_model = DescribeFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIndexJobStatusRequest(TeaModel):
    def __init__(
        self,
        index_id: str = None,
        job_id: str = None,
    ):
        # This parameter is required.
        self.index_id = index_id
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetIndexJobStatusResponseBodyDataDocuments(TeaModel):
    def __init__(
        self,
        code: str = None,
        doc_id: str = None,
        doc_name: str = None,
        message: str = None,
        status: str = None,
    ):
        self.code = code
        self.doc_id = doc_id
        self.doc_name = doc_name
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetIndexJobStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        documents: List[GetIndexJobStatusResponseBodyDataDocuments] = None,
        job_id: str = None,
        status: str = None,
    ):
        self.documents = documents
        self.job_id = job_id
        self.status = status

    def validate(self):
        if self.documents:
            for k in self.documents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Documents'] = []
        if self.documents is not None:
            for k in self.documents:
                result['Documents'].append(k.to_map() if k else None)
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.documents = []
        if m.get('Documents') is not None:
            for k in m.get('Documents'):
                temp_model = GetIndexJobStatusResponseBodyDataDocuments()
                self.documents.append(temp_model.from_map(k))
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetIndexJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetIndexJobStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetIndexJobStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetIndexJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIndexJobStatusResponseBody = None,
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
            temp_model = GetIndexJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetrieveRequestRerank(TeaModel):
    def __init__(
        self,
        model_name: str = None,
    ):
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        return self


class RetrieveRequestRewrite(TeaModel):
    def __init__(
        self,
        model_name: str = None,
    ):
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        return self


class RetrieveRequest(TeaModel):
    def __init__(
        self,
        dense_similarity_top_k: int = None,
        enable_reranking: bool = None,
        enable_rewrite: bool = None,
        index_id: str = None,
        query: str = None,
        rerank: List[RetrieveRequestRerank] = None,
        rerank_min_score: float = None,
        rerank_top_n: int = None,
        rewrite: List[RetrieveRequestRewrite] = None,
        save_retriever_history: bool = None,
        sparse_similarity_top_k: int = None,
    ):
        self.dense_similarity_top_k = dense_similarity_top_k
        self.enable_reranking = enable_reranking
        self.enable_rewrite = enable_rewrite
        # This parameter is required.
        self.index_id = index_id
        self.query = query
        self.rerank = rerank
        self.rerank_min_score = rerank_min_score
        self.rerank_top_n = rerank_top_n
        self.rewrite = rewrite
        self.save_retriever_history = save_retriever_history
        self.sparse_similarity_top_k = sparse_similarity_top_k

    def validate(self):
        if self.rerank:
            for k in self.rerank:
                if k:
                    k.validate()
        if self.rewrite:
            for k in self.rewrite:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dense_similarity_top_k is not None:
            result['DenseSimilarityTopK'] = self.dense_similarity_top_k
        if self.enable_reranking is not None:
            result['EnableReranking'] = self.enable_reranking
        if self.enable_rewrite is not None:
            result['EnableRewrite'] = self.enable_rewrite
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.query is not None:
            result['Query'] = self.query
        result['Rerank'] = []
        if self.rerank is not None:
            for k in self.rerank:
                result['Rerank'].append(k.to_map() if k else None)
        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score
        if self.rerank_top_n is not None:
            result['RerankTopN'] = self.rerank_top_n
        result['Rewrite'] = []
        if self.rewrite is not None:
            for k in self.rewrite:
                result['Rewrite'].append(k.to_map() if k else None)
        if self.save_retriever_history is not None:
            result['SaveRetrieverHistory'] = self.save_retriever_history
        if self.sparse_similarity_top_k is not None:
            result['SparseSimilarityTopK'] = self.sparse_similarity_top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DenseSimilarityTopK') is not None:
            self.dense_similarity_top_k = m.get('DenseSimilarityTopK')
        if m.get('EnableReranking') is not None:
            self.enable_reranking = m.get('EnableReranking')
        if m.get('EnableRewrite') is not None:
            self.enable_rewrite = m.get('EnableRewrite')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        self.rerank = []
        if m.get('Rerank') is not None:
            for k in m.get('Rerank'):
                temp_model = RetrieveRequestRerank()
                self.rerank.append(temp_model.from_map(k))
        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')
        if m.get('RerankTopN') is not None:
            self.rerank_top_n = m.get('RerankTopN')
        self.rewrite = []
        if m.get('Rewrite') is not None:
            for k in m.get('Rewrite'):
                temp_model = RetrieveRequestRewrite()
                self.rewrite.append(temp_model.from_map(k))
        if m.get('SaveRetrieverHistory') is not None:
            self.save_retriever_history = m.get('SaveRetrieverHistory')
        if m.get('SparseSimilarityTopK') is not None:
            self.sparse_similarity_top_k = m.get('SparseSimilarityTopK')
        return self


class RetrieveShrinkRequest(TeaModel):
    def __init__(
        self,
        dense_similarity_top_k: int = None,
        enable_reranking: bool = None,
        enable_rewrite: bool = None,
        index_id: str = None,
        query: str = None,
        rerank_shrink: str = None,
        rerank_min_score: float = None,
        rerank_top_n: int = None,
        rewrite_shrink: str = None,
        save_retriever_history: bool = None,
        sparse_similarity_top_k: int = None,
    ):
        self.dense_similarity_top_k = dense_similarity_top_k
        self.enable_reranking = enable_reranking
        self.enable_rewrite = enable_rewrite
        # This parameter is required.
        self.index_id = index_id
        self.query = query
        self.rerank_shrink = rerank_shrink
        self.rerank_min_score = rerank_min_score
        self.rerank_top_n = rerank_top_n
        self.rewrite_shrink = rewrite_shrink
        self.save_retriever_history = save_retriever_history
        self.sparse_similarity_top_k = sparse_similarity_top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dense_similarity_top_k is not None:
            result['DenseSimilarityTopK'] = self.dense_similarity_top_k
        if self.enable_reranking is not None:
            result['EnableReranking'] = self.enable_reranking
        if self.enable_rewrite is not None:
            result['EnableRewrite'] = self.enable_rewrite
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.query is not None:
            result['Query'] = self.query
        if self.rerank_shrink is not None:
            result['Rerank'] = self.rerank_shrink
        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score
        if self.rerank_top_n is not None:
            result['RerankTopN'] = self.rerank_top_n
        if self.rewrite_shrink is not None:
            result['Rewrite'] = self.rewrite_shrink
        if self.save_retriever_history is not None:
            result['SaveRetrieverHistory'] = self.save_retriever_history
        if self.sparse_similarity_top_k is not None:
            result['SparseSimilarityTopK'] = self.sparse_similarity_top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DenseSimilarityTopK') is not None:
            self.dense_similarity_top_k = m.get('DenseSimilarityTopK')
        if m.get('EnableReranking') is not None:
            self.enable_reranking = m.get('EnableReranking')
        if m.get('EnableRewrite') is not None:
            self.enable_rewrite = m.get('EnableRewrite')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Rerank') is not None:
            self.rerank_shrink = m.get('Rerank')
        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')
        if m.get('RerankTopN') is not None:
            self.rerank_top_n = m.get('RerankTopN')
        if m.get('Rewrite') is not None:
            self.rewrite_shrink = m.get('Rewrite')
        if m.get('SaveRetrieverHistory') is not None:
            self.save_retriever_history = m.get('SaveRetrieverHistory')
        if m.get('SparseSimilarityTopK') is not None:
            self.sparse_similarity_top_k = m.get('SparseSimilarityTopK')
        return self


class RetrieveResponseBodyDataNodes(TeaModel):
    def __init__(
        self,
        metadata: Any = None,
        score: float = None,
        text: str = None,
    ):
        self.metadata = metadata
        self.score = score
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.score is not None:
            result['Score'] = self.score
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RetrieveResponseBodyData(TeaModel):
    def __init__(
        self,
        nodes: List[RetrieveResponseBodyDataNodes] = None,
    ):
        self.nodes = nodes

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = RetrieveResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class RetrieveResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RetrieveResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RetrieveResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RetrieveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RetrieveResponseBody = None,
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
            temp_model = RetrieveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitIndexAddDocumentsJobRequest(TeaModel):
    def __init__(
        self,
        category_ids: List[str] = None,
        document_ids: List[str] = None,
        index_id: str = None,
        source_type: str = None,
    ):
        self.category_ids = category_ids
        self.document_ids = document_ids
        # This parameter is required.
        self.index_id = index_id
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.document_ids is not None:
            result['DocumentIds'] = self.document_ids
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('DocumentIds') is not None:
            self.document_ids = m.get('DocumentIds')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SubmitIndexAddDocumentsJobShrinkRequest(TeaModel):
    def __init__(
        self,
        category_ids_shrink: str = None,
        document_ids_shrink: str = None,
        index_id: str = None,
        source_type: str = None,
    ):
        self.category_ids_shrink = category_ids_shrink
        self.document_ids_shrink = document_ids_shrink
        # This parameter is required.
        self.index_id = index_id
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink
        if self.document_ids_shrink is not None:
            result['DocumentIds'] = self.document_ids_shrink
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryIds') is not None:
            self.category_ids_shrink = m.get('CategoryIds')
        if m.get('DocumentIds') is not None:
            self.document_ids_shrink = m.get('DocumentIds')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SubmitIndexAddDocumentsJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitIndexAddDocumentsJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitIndexAddDocumentsJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SubmitIndexAddDocumentsJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitIndexAddDocumentsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitIndexAddDocumentsJobResponseBody = None,
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
            temp_model = SubmitIndexAddDocumentsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitIndexJobRequest(TeaModel):
    def __init__(
        self,
        index_id: str = None,
    ):
        # This parameter is required.
        self.index_id = index_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        return self


class SubmitIndexJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        index_id: str = None,
    ):
        self.id = id
        self.index_id = index_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        return self


class SubmitIndexJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitIndexJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SubmitIndexJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitIndexJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitIndexJobResponseBody = None,
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
            temp_model = SubmitIndexJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


