# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class ListKeywordLibsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListKeywordLibsResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # Returned data.
        self.data = data
        # Further description of the error code.
        self.msg = msg
        # ID assigned by the backend to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id
        # Success indicator.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListKeywordLibsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListKeywordLibsResponseBodyData(DaraModel):
    def __init__(
        self,
        gmt_modified: str = None,
        keyword_count: str = None,
        lib_id: str = None,
        lib_name: str = None,
        service_codes: str = None,
        uid: str = None,
    ):
        # Modification time.
        self.gmt_modified = gmt_modified
        # Number of keywords.
        self.keyword_count = keyword_count
        # Library ID.
        self.lib_id = lib_id
        # Library name.
        self.lib_name = lib_name
        # Service codes.
        self.service_codes = service_codes
        # UID.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.keyword_count is not None:
            result['KeywordCount'] = self.keyword_count

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.lib_name is not None:
            result['LibName'] = self.lib_name

        if self.service_codes is not None:
            result['ServiceCodes'] = self.service_codes

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('KeywordCount') is not None:
            self.keyword_count = m.get('KeywordCount')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')

        if m.get('ServiceCodes') is not None:
            self.service_codes = m.get('ServiceCodes')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

