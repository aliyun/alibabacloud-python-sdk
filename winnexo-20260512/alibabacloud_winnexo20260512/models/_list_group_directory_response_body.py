# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListGroupDirectoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListGroupDirectoryResponseBodyItems] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The immediate subdirectories and resources on the current page. The queried directory itself is not included, and results are not recursively expanded.
        self.items = items
        # The error description.
        self.message = message
        # The current page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The request trace ID.
        self.request_id = request_id
        # The total number of entries after filtering and before pagination. This includes both physical content and referenced content that match the filter criteria.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListGroupDirectoryResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListGroupDirectoryResponseBodyItems(DaraModel):
    def __init__(
        self,
        creator_name: str = None,
        directory_kind: str = None,
        directory_type: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        item_id: str = None,
        item_type: str = None,
        modifier_name: str = None,
        name: str = None,
        object_bindings: List[main_models.ListGroupDirectoryResponseBodyItemsObjectBindings] = None,
        read_only: bool = None,
        source_kind: str = None,
        source_status: str = None,
        source_type: str = None,
    ):
        # The name of the directory creator or resource submitter.
        self.creator_name = creator_name
        # The directory ownership category. This follows the service output, such as normal.
        self.directory_kind = directory_kind
        # The directory type. Physical directories within the space have a value of GROUP. Reference directories retain their original type.
        self.directory_type = directory_type
        # The creation timestamp, in seconds.
        self.gmt_create = gmt_create
        # The modification timestamp, in seconds.
        self.gmt_modified = gmt_modified
        # The directoryId of a directory or the sourceId of a resource.
        self.item_id = item_id
        # The content type. Valid values: directory (subdirectory) and resource.
        self.item_type = item_type
        # The name of the last modifier.
        self.modifier_name = modifier_name
        # The content name.
        self.name = name
        # The list of resource object bindings. This may be empty if metadata is missing or for referenced resources.
        self.object_bindings = object_bindings
        # Indicates whether the content is a read-only reference. A value of false does not indicate write permissions. Write operations still require creator or space administrator permissions.
        self.read_only = read_only
        # The resource ownership category. This follows the service output.
        self.source_kind = source_kind
        # The resource parsing status. This field has a value only for resource items.
        self.source_status = source_status
        # The resource type. This field has a value only for resource items. The type display rules of the service are used.
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

        if self.directory_kind is not None:
            result['directoryKind'] = self.directory_kind

        if self.directory_type is not None:
            result['directoryType'] = self.directory_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.item_id is not None:
            result['itemId'] = self.item_id

        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name

        if self.name is not None:
            result['name'] = self.name

        result['objectBindings'] = []
        if self.object_bindings is not None:
            for k1 in self.object_bindings:
                result['objectBindings'].append(k1.to_map() if k1 else None)

        if self.read_only is not None:
            result['readOnly'] = self.read_only

        if self.source_kind is not None:
            result['sourceKind'] = self.source_kind

        if self.source_status is not None:
            result['sourceStatus'] = self.source_status

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('directoryKind') is not None:
            self.directory_kind = m.get('directoryKind')

        if m.get('directoryType') is not None:
            self.directory_type = m.get('directoryType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')

        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.object_bindings = []
        if m.get('objectBindings') is not None:
            for k1 in m.get('objectBindings'):
                temp_model = main_models.ListGroupDirectoryResponseBodyItemsObjectBindings()
                self.object_bindings.append(temp_model.from_map(k1))

        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')

        if m.get('sourceKind') is not None:
            self.source_kind = m.get('sourceKind')

        if m.get('sourceStatus') is not None:
            self.source_status = m.get('sourceStatus')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

class ListGroupDirectoryResponseBodyItemsObjectBindings(DaraModel):
    def __init__(
        self,
        graph_name: str = None,
        object_id: str = None,
        object_name: str = None,
        object_type: str = None,
        object_type_name: str = None,
    ):
        # The name of the knowledge graph to which the binding belongs.
        self.graph_name = graph_name
        # The business ID of the object.
        self.object_id = object_id
        # The display name of the object.
        self.object_name = object_name
        # The object type.
        self.object_type = object_type
        # The display name of the object type.
        self.object_type_name = object_type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.graph_name is not None:
            result['graphName'] = self.graph_name

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
        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('objectTypeName') is not None:
            self.object_type_name = m.get('objectTypeName')

        return self

