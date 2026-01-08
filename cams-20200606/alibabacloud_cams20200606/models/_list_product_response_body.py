# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListProductResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: main_models.ListProductResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The returned data.
        self.model = model
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.ListProductResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListProductResponseBodyModel(DaraModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
        paging: main_models.ListProductResponseBodyModelPaging = None,
    ):
        # The returned data.
        self.data = data
        # The pagination details.
        self.paging = paging

    def validate(self):
        if self.paging:
            self.paging.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.paging is not None:
            result['Paging'] = self.paging.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Paging') is not None:
            temp_model = main_models.ListProductResponseBodyModelPaging()
            self.paging = temp_model.from_map(m.get('Paging'))

        return self

class ListProductResponseBodyModelPaging(DaraModel):
    def __init__(
        self,
        cursors: main_models.ListProductResponseBodyModelPagingCursors = None,
    ):
        # The cursors for pagination.
        self.cursors = cursors

    def validate(self):
        if self.cursors:
            self.cursors.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cursors is not None:
            result['Cursors'] = self.cursors.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cursors') is not None:
            temp_model = main_models.ListProductResponseBodyModelPagingCursors()
            self.cursors = temp_model.from_map(m.get('Cursors'))

        return self

class ListProductResponseBodyModelPagingCursors(DaraModel):
    def __init__(
        self,
        after: str = None,
        before: str = None,
    ):
        # The cursor that points to the end of the page of the returned data.
        self.after = after
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after is not None:
            result['After'] = self.after

        if self.before is not None:
            result['Before'] = self.before

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')

        if m.get('Before') is not None:
            self.before = m.get('Before')

        return self

