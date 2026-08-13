# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListPersonalDirectoryContentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListPersonalDirectoryContentsResponseBodyItems] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        self.items = items
        # 错误描述，成功时为空
        self.message = message
        # 当前页码
        self.page = page
        # 每页数量
        self.page_size = page_size
        # 请求追踪 ID
        self.request_id = request_id
        # 总数（不分页前的命中行数）
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListPersonalDirectoryContentsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListPersonalDirectoryContentsResponseBodyItems(DaraModel):
    def __init__(
        self,
        creator_name: str = None,
        description: str = None,
        directory_kind: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        item_id: str = None,
        item_type: str = None,
        name: str = None,
        object_bindings: List[main_models.ListPersonalDirectoryContentsResponseBodyItemsObjectBindings] = None,
        source_failed_count: int = None,
        source_kind: str = None,
        source_ready_count: int = None,
        source_status: str = None,
        source_total_count: int = None,
        source_type: str = None,
    ):
        # 目录创建者姓名（仅 directoryId=\"root\" 列表时返回）
        self.creator_name = creator_name
        # 知识库描述（仅 directoryId=\"root\" 列表时返回）
        self.description = description
        # 目录 KB 归属类型（itemType=directory 时有值）：aliding_kb_root / aliding_kb_internal / normal
        self.directory_kind = directory_kind
        # 创建时间戳（毫秒）
        self.gmt_create = gmt_create
        # 修改时间戳（毫秒）
        self.gmt_modified = gmt_modified
        # 唯一标识（目录为 directoryId，资源为 sourceId）
        self.item_id = item_id
        # 类型: directory 或 resource
        self.item_type = item_type
        # 文件名
        self.name = name
        self.object_bindings = object_bindings
        # 目录下失败资源数（含子目录，仅 directoryId=\"root\" 列表时返回）
        self.source_failed_count = source_failed_count
        # Source KB 归属类型（itemType=resource 时有值）：aliding_kb_doc / normal
        self.source_kind = source_kind
        # 目录下成功资源数（含子目录，仅 directoryId=\"root\" 列表时返回）
        self.source_ready_count = source_ready_count
        # 资源状态（itemType=resource 时有值）
        self.source_status = source_status
        # 目录下资源总数（含子目录，仅 directoryId=\"root\" 列表时返回）
        self.source_total_count = source_total_count
        # 资源类型（itemType=resource 时有值；产出保存类资源会被反刷为 OUTPUT）
        self.source_type = source_type

    def validate(self):
        if self.object_bindings:
            for v1 in self.object_bindings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.description is not None:
            result['description'] = self.description

        if self.directory_kind is not None:
            result['directoryKind'] = self.directory_kind

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.item_id is not None:
            result['itemId'] = self.item_id

        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.name is not None:
            result['name'] = self.name

        result['objectBindings'] = []
        if self.object_bindings is not None:
            for k1 in self.object_bindings:
                result['objectBindings'].append(k1.to_map() if k1 else None)

        if self.source_failed_count is not None:
            result['sourceFailedCount'] = self.source_failed_count

        if self.source_kind is not None:
            result['sourceKind'] = self.source_kind

        if self.source_ready_count is not None:
            result['sourceReadyCount'] = self.source_ready_count

        if self.source_status is not None:
            result['sourceStatus'] = self.source_status

        if self.source_total_count is not None:
            result['sourceTotalCount'] = self.source_total_count

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryKind') is not None:
            self.directory_kind = m.get('directoryKind')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')

        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.object_bindings = []
        if m.get('objectBindings') is not None:
            for k1 in m.get('objectBindings'):
                temp_model = main_models.ListPersonalDirectoryContentsResponseBodyItemsObjectBindings()
                self.object_bindings.append(temp_model.from_map(k1))

        if m.get('sourceFailedCount') is not None:
            self.source_failed_count = m.get('sourceFailedCount')

        if m.get('sourceKind') is not None:
            self.source_kind = m.get('sourceKind')

        if m.get('sourceReadyCount') is not None:
            self.source_ready_count = m.get('sourceReadyCount')

        if m.get('sourceStatus') is not None:
            self.source_status = m.get('sourceStatus')

        if m.get('sourceTotalCount') is not None:
            self.source_total_count = m.get('sourceTotalCount')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

class ListPersonalDirectoryContentsResponseBodyItemsObjectBindings(DaraModel):
    def __init__(
        self,
        object_id: str = None,
        object_name: str = None,
        object_type: str = None,
        object_type_name: str = None,
    ):
        # 对象唯一 ID
        self.object_id = object_id
        # 对象显示名（如客户名称），由图谱 schema 解析；缓存缺失时为 null
        self.object_name = object_name
        # 对象类型（如 customer / opportunity），对应图谱 schema 中的 object_type
        self.object_type = object_type
        # 对象类型显示名（如"客户"），由图谱 schema 解析；缓存缺失时为 null
        self.object_type_name = object_type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_name is not None:
            result['objectName'] = self.object_name

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.object_type_name is not None:
            result['objectTypeName'] = self.object_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('objectTypeName') is not None:
            self.object_type_name = m.get('objectTypeName')

        return self

