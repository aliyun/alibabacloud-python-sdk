# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetKeywordLibResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetKeywordLibResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The description of the error code.
        self.msg = msg
        # The request ID assigned by the backend, which uniquely identifies the request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.GetKeywordLibResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetKeywordLibResponseBodyData(DaraModel):
    def __init__(
        self,
        gmt_modified: str = None,
        keyword_count: str = None,
        lib_id: str = None,
        lib_name: str = None,
        uid: str = None,
    ):
        # The last modification time.
        self.gmt_modified = gmt_modified
        # The number of keywords.
        self.keyword_count = keyword_count
        # The keyword library ID.
        self.lib_id = lib_id
        # The library name.
        self.lib_name = lib_name
        # The Alibaba Cloud account ID.
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

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

