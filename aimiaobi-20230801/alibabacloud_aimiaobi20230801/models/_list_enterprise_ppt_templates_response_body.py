# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListEnterprisePptTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[main_models.ListEnterprisePptTemplatesResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The status code.
        self.code = code
        # The current page number.
        self.current = current
        # An array of enterprise-specific PPT template objects.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The maximum number of results per page, as specified in the request. Note: This parameter is not yet in effect.
        self.max_results = max_results
        # The response message.
        self.message = message
        # The token for the next page of results. An empty value indicates that no more data is available. Note: This parameter is not yet in effect.
        self.next_token = next_token
        # The unique request ID. Provide this ID when you contact technical support.
        self.request_id = request_id
        # The number of entries returned on the current page (the \\"page size\\").
        self.size = size
        # Indicates whether the request succeeded. `true` indicates success, and `false` indicates failure.
        self.success = success
        # The total number of entries that match the query.
        self.total_count = total_count

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

        if self.current is not None:
            result['Current'] = self.current

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListEnterprisePptTemplatesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEnterprisePptTemplatesResponseBodyData(DaraModel):
    def __init__(
        self,
        cover_img: str = None,
        id: int = None,
    ):
        # The URL of the cover image.
        self.cover_img = cover_img
        # The ID of the template.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_img is not None:
            result['CoverImg'] = self.cover_img

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverImg') is not None:
            self.cover_img = m.get('CoverImg')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

