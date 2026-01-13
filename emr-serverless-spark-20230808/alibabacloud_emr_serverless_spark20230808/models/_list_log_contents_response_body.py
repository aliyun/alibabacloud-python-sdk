# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListLogContentsResponseBody(DaraModel):
    def __init__(
        self,
        list_log_content: main_models.ListLogContentsResponseBodyListLogContent = None,
        request_id: str = None,
    ):
        # Log content.
        self.list_log_content = list_log_content
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.list_log_content:
            self.list_log_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_log_content is not None:
            result['listLogContent'] = self.list_log_content.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('listLogContent') is not None:
            temp_model = main_models.ListLogContentsResponseBodyListLogContent()
            self.list_log_content = temp_model.from_map(m.get('listLogContent'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListLogContentsResponseBodyListLogContent(DaraModel):
    def __init__(
        self,
        contents: List[main_models.ListLogContentsResponseBodyListLogContentContents] = None,
        total_length: int = None,
    ):
        # List of log line contents.
        self.contents = contents
        # Total number of log lines.
        self.total_length = total_length

    def validate(self):
        if self.contents:
            for v1 in self.contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['contents'] = []
        if self.contents is not None:
            for k1 in self.contents:
                result['contents'].append(k1.to_map() if k1 else None)

        if self.total_length is not None:
            result['totalLength'] = self.total_length

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contents = []
        if m.get('contents') is not None:
            for k1 in m.get('contents'):
                temp_model = main_models.ListLogContentsResponseBodyListLogContentContents()
                self.contents.append(temp_model.from_map(k1))

        if m.get('totalLength') is not None:
            self.total_length = m.get('totalLength')

        return self

class ListLogContentsResponseBodyListLogContentContents(DaraModel):
    def __init__(
        self,
        line_content: str = None,
    ):
        # Log line content.
        self.line_content = line_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line_content is not None:
            result['LineContent'] = self.line_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineContent') is not None:
            self.line_content = m.get('LineContent')

        return self

