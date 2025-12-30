# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QuerySearchLibResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        index_info: List[main_models.QuerySearchLibResponseBodyIndexInfo] = None,
        request_id: str = None,
        search_lib_config: str = None,
        search_lib_name: str = None,
        status: str = None,
        success: str = None,
    ):
        # The status code returned.
        self.code = code
        self.index_info = index_info
        # The ID of the request.
        self.request_id = request_id
        self.search_lib_config = search_lib_config
        # The name of the search library.
        self.search_lib_name = search_lib_name
        # The status of the search library.
        # 
        # Valid values:
        # 
        # *   normal
        # *   deleting
        # *   deleteFail
        self.status = status
        # Indicates whether the call was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.index_info:
            for v1 in self.index_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['IndexInfo'] = []
        if self.index_info is not None:
            for k1 in self.index_info:
                result['IndexInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.search_lib_config is not None:
            result['SearchLibConfig'] = self.search_lib_config

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.index_info = []
        if m.get('IndexInfo') is not None:
            for k1 in m.get('IndexInfo'):
                temp_model = main_models.QuerySearchLibResponseBodyIndexInfo()
                self.index_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SearchLibConfig') is not None:
            self.search_lib_config = m.get('SearchLibConfig')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySearchLibResponseBodyIndexInfo(DaraModel):
    def __init__(
        self,
        index_readiness: str = None,
        index_status: str = None,
        index_type: str = None,
    ):
        self.index_readiness = index_readiness
        self.index_status = index_status
        self.index_type = index_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_readiness is not None:
            result['IndexReadiness'] = self.index_readiness

        if self.index_status is not None:
            result['IndexStatus'] = self.index_status

        if self.index_type is not None:
            result['IndexType'] = self.index_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexReadiness') is not None:
            self.index_readiness = m.get('IndexReadiness')

        if m.get('IndexStatus') is not None:
            self.index_status = m.get('IndexStatus')

        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')

        return self

