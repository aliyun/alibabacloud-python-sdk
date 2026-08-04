# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ScgSearchRequest(DaraModel):
    def __init__(
        self,
        scg_filter: main_models.ScgSearchRequestScgFilter = None,
        topic_id: str = None,
    ):
        # Query filter
        # 
        # This parameter is required.
        self.scg_filter = scg_filter
        # Selection pool ID. Optional values: MC201132 (Ethnic Chinese Style), MC201136 (Pop Music), MC201139 (Sweet Love), MC201133 (Folk), MC201137 (Relaxing Reading), MC201138 (Happiness), PA202029 (Stories), PA202030 (Children\\"s Songs), PA202028 (Chinese Classics and History), PA202032 (Encyclopedia), PA202031 (English Children\\"s Songs)
        # 
        # This parameter is required.
        self.topic_id = topic_id

    def validate(self):
        if self.scg_filter:
            self.scg_filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scg_filter is not None:
            result['ScgFilter'] = self.scg_filter.to_map()

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScgFilter') is not None:
            temp_model = main_models.ScgSearchRequestScgFilter()
            self.scg_filter = temp_model.from_map(m.get('ScgFilter'))

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        return self

class ScgSearchRequestScgFilter(DaraModel):
    def __init__(
        self,
        off_set_param: main_models.ScgSearchRequestScgFilterOffSetParam = None,
        page_param: main_models.ScgSearchRequestScgFilterPageParam = None,
        sort_param: main_models.ScgSearchRequestScgFilterSortParam = None,
        use_off_set: bool = None,
    ):
        # Paging type
        self.off_set_param = off_set_param
        # Paging type
        self.page_param = page_param
        # Sorting parameters
        # 
        # This parameter is required.
        self.sort_param = sort_param
        # Whether to use the pageParam object for paging. Choose either offSetParam or pageParam. The default paging mode is pageParam.
        # 
        # This parameter is required.
        self.use_off_set = use_off_set

    def validate(self):
        if self.off_set_param:
            self.off_set_param.validate()
        if self.page_param:
            self.page_param.validate()
        if self.sort_param:
            self.sort_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.off_set_param is not None:
            result['OffSetParam'] = self.off_set_param.to_map()

        if self.page_param is not None:
            result['PageParam'] = self.page_param.to_map()

        if self.sort_param is not None:
            result['SortParam'] = self.sort_param.to_map()

        if self.use_off_set is not None:
            result['UseOffSet'] = self.use_off_set

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OffSetParam') is not None:
            temp_model = main_models.ScgSearchRequestScgFilterOffSetParam()
            self.off_set_param = temp_model.from_map(m.get('OffSetParam'))

        if m.get('PageParam') is not None:
            temp_model = main_models.ScgSearchRequestScgFilterPageParam()
            self.page_param = temp_model.from_map(m.get('PageParam'))

        if m.get('SortParam') is not None:
            temp_model = main_models.ScgSearchRequestScgFilterSortParam()
            self.sort_param = temp_model.from_map(m.get('SortParam'))

        if m.get('UseOffSet') is not None:
            self.use_off_set = m.get('UseOffSet')

        return self

class ScgSearchRequestScgFilterSortParam(DaraModel):
    def __init__(
        self,
        sort_key: str = None,
        sort_order: str = None,
        sort_text: str = None,
    ):
        # Sorting field
        self.sort_key = sort_key
        # Sorting order
        self.sort_order = sort_order
        # Sorting field (default: empty string)
        self.sort_text = sort_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.sort_text is not None:
            result['SortText'] = self.sort_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('SortText') is not None:
            self.sort_text = m.get('SortText')

        return self

class ScgSearchRequestScgFilterPageParam(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        # Page number
        self.page_num = page_num
        # Number of records per page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ScgSearchRequestScgFilterOffSetParam(DaraModel):
    def __init__(
        self,
        limit: int = None,
        offset: int = None,
    ):
        # Number of returned items
        self.limit = limit
        # Number of skipped items
        self.offset = offset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['Limit'] = self.limit

        if self.offset is not None:
            result['Offset'] = self.offset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        return self

