# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeVariableListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeVariableListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10.
        self.page_size = page_size
        # Returned object.
        self.result_object = result_object
        # Total number of items.
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeVariableListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeVariableListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        define_id: str = None,
        description: str = None,
        extend_info: Dict[str, Any] = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        left_capacity: int = None,
        name: str = None,
        outputs_type: str = None,
        ref_obj_id: str = None,
        ref_obj_name: str = None,
        ref_obj_type: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        user_id: int = None,
    ):
        # Capacity.
        self.capacity = capacity
        # Variable definition ID.
        self.define_id = define_id
        # Description information.
        self.description = description
        # Extended information.
        self.extend_info = extend_info
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Variable ID.
        self.id = id
        # Remaining capacity.
        self.left_capacity = left_capacity
        # Variable name
        self.name = name
        # Variable output type
        self.outputs_type = outputs_type
        # Associated event ID.
        self.ref_obj_id = ref_obj_id
        # Associated event name.
        self.ref_obj_name = ref_obj_name
        # Associated object type of the variable
        self.ref_obj_type = ref_obj_type
        # Source type.
        self.source_type = source_type
        # Title.
        self.title = title
        # Variable type.
        self.type = type
        # User ID to which the data belongs.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['capacity'] = self.capacity

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.left_capacity is not None:
            result['leftCapacity'] = self.left_capacity

        if self.name is not None:
            result['name'] = self.name

        if self.outputs_type is not None:
            result['outputsType'] = self.outputs_type

        if self.ref_obj_id is not None:
            result['refObjId'] = self.ref_obj_id

        if self.ref_obj_name is not None:
            result['refObjName'] = self.ref_obj_name

        if self.ref_obj_type is not None:
            result['refObjType'] = self.ref_obj_type

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('leftCapacity') is not None:
            self.left_capacity = m.get('leftCapacity')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outputsType') is not None:
            self.outputs_type = m.get('outputsType')

        if m.get('refObjId') is not None:
            self.ref_obj_id = m.get('refObjId')

        if m.get('refObjName') is not None:
            self.ref_obj_name = m.get('refObjName')

        if m.get('refObjType') is not None:
            self.ref_obj_type = m.get('refObjType')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

