# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryDataServiceListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryDataServiceListResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return result.
        self.result = result
        # Indicates whether the request was successful. Value range:
        # - true: The request was successful 
        # - false: The request failed
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryDataServiceListResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDataServiceListResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryDataServiceListResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # Data service information.
        self.data = data
        # Page number.
        self.page_num = page_num
        # Number of records per page.
        self.page_size = page_size
        # Total number of rows.
        self.total_num = total_num
        # Total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryDataServiceListResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class QueryDataServiceListResponseBodyResultData(DaraModel):
    def __init__(
        self,
        content: main_models.QueryDataServiceListResponseBodyResultDataContent = None,
        creator_id: str = None,
        creator_name: str = None,
        cube_id: str = None,
        cube_name: str = None,
        desc: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        modifier_id: str = None,
        modifier_name: str = None,
        name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        sid: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The model of the data service in JSON format.
        self.content = content
        # Creator ID.
        self.creator_id = creator_id
        # Creator\\"s name.
        self.creator_name = creator_name
        # Cube identifier ID.
        self.cube_id = cube_id
        # Dataset name.
        self.cube_name = cube_name
        # Description
        self.desc = desc
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Modifier\\"s userId.
        self.modifier_id = modifier_id
        # Modifier\\"s name
        self.modifier_name = modifier_name
        # Data service name.
        self.name = name
        # Owner ID
        self.owner_id = owner_id
        # Owner\\"s name
        self.owner_name = owner_name
        # Unique ID of the data service.
        self.sid = sid
        # Workspace ID.
        self.workspace_id = workspace_id
        # Workspace name.
        self.workspace_name = workspace_name

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.cube_id is not None:
            result['CubeId'] = self.cube_id

        if self.cube_name is not None:
            result['CubeName'] = self.cube_name

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.modifier_name is not None:
            result['ModifierName'] = self.modifier_name

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.sid is not None:
            result['Sid'] = self.sid

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.QueryDataServiceListResponseBodyResultDataContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')

        if m.get('CubeName') is not None:
            self.cube_name = m.get('CubeName')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('ModifierName') is not None:
            self.modifier_name = m.get('ModifierName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

class QueryDataServiceListResponseBodyResultDataContent(DaraModel):
    def __init__(
        self,
        cube_id: str = None,
        cube_name: str = None,
        detail: bool = None,
        filter: main_models.QueryDataServiceListResponseBodyResultDataContentFilter = None,
        return_fields: List[main_models.QueryDataServiceListResponseBodyResultDataContentReturnFields] = None,
    ):
        # Cube identifier ID.
        self.cube_id = cube_id
        # Dataset name.
        self.cube_name = cube_name
        # Detail or Summary
        self.detail = detail
        # Request parameter information.
        self.filter = filter
        # Return information.
        self.return_fields = return_fields

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.return_fields:
            for v1 in self.return_fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id

        if self.cube_name is not None:
            result['CubeName'] = self.cube_name

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        result['ReturnFields'] = []
        if self.return_fields is not None:
            for k1 in self.return_fields:
                result['ReturnFields'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')

        if m.get('CubeName') is not None:
            self.cube_name = m.get('CubeName')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('Filter') is not None:
            temp_model = main_models.QueryDataServiceListResponseBodyResultDataContentFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        self.return_fields = []
        if m.get('ReturnFields') is not None:
            for k1 in m.get('ReturnFields'):
                temp_model = main_models.QueryDataServiceListResponseBodyResultDataContentReturnFields()
                self.return_fields.append(temp_model.from_map(k1))

        return self

class QueryDataServiceListResponseBodyResultDataContentReturnFields(DaraModel):
    def __init__(
        self,
        aggregator: str = None,
        alias: str = None,
        desc: str = None,
        field: main_models.QueryDataServiceListResponseBodyResultDataContentReturnFieldsField = None,
        orderby: str = None,
    ):
        # Aggregation operator. For example, SUM, AVG, and MAX.
        self.aggregator = aggregator
        # Field parameter name.
        self.alias = alias
        # Remark for the returned field.
        self.desc = desc
        # Corresponding cube field information.
        self.field = field
        # Sorting.
        # 
        # - asc: Ascending
        # - desc: Descending
        # - no: No sorting
        self.orderby = orderby

    def validate(self):
        if self.field:
            self.field.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator

        if self.alias is not None:
            result['Alias'] = self.alias

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.field is not None:
            result['Field'] = self.field.to_map()

        if self.orderby is not None:
            result['Orderby'] = self.orderby

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')

        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Field') is not None:
            temp_model = main_models.QueryDataServiceListResponseBodyResultDataContentReturnFieldsField()
            self.field = temp_model.from_map(m.get('Field'))

        if m.get('Orderby') is not None:
            self.orderby = m.get('Orderby')

        return self

class QueryDataServiceListResponseBodyResultDataContentReturnFieldsField(DaraModel):
    def __init__(
        self,
        caption: str = None,
        column: str = None,
        data_type: str = None,
        fid: str = None,
        granularity: str = None,
        name: str = None,
        type: str = None,
    ):
        # Display name in the cube model (can be in Chinese or English).
        self.caption = caption
        # The corresponding physical field name.
        self.column = column
        # Data type.
        # 
        # - number: numeric
        # - string: string
        # - date: date
        # - datetime: datetime
        # - time: time
        # - geographic: geographic
        # - boolean: boolean
        # - url: URL
        self.data_type = data_type
        # Unique identifier for the original field.
        self.fid = fid
        # This attribute is included for date and geographic dimensions, indicating the supported granularity.
        self.granularity = granularity
        # Unique name of the cube field, mainly used for unique positioning in the returned result.
        self.name = name
        # Type.
        # 
        # - Dimension: Dimension
        # - Measure: Measure
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption

        if self.column is not None:
            result['Column'] = self.column

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.fid is not None:
            result['Fid'] = self.fid

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Fid') is not None:
            self.fid = m.get('Fid')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class QueryDataServiceListResponseBodyResultDataContentFilter(DaraModel):
    def __init__(
        self,
        filters: List[Dict[str, Any]] = None,
        logical_operator: str = None,
        type: str = None,
    ):
        # Combined conditions.
        self.filters = filters
        # Logical relationship between multiple SQL text keywords.
        # 
        # - **or**: or
        # - **and**: and
        self.logical_operator = logical_operator
        # Type.
        # 
        # - basic: basic
        # - combined: complex
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filters is not None:
            result['Filters'] = self.filters

        if self.logical_operator is not None:
            result['LogicalOperator'] = self.logical_operator

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')

        if m.get('LogicalOperator') is not None:
            self.logical_operator = m.get('LogicalOperator')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

