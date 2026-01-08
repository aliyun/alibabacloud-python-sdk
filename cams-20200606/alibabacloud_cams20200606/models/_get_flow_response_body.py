# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class GetFlowResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetFlowResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetFlowResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFlowResponseBodyData(DaraModel):
    def __init__(
        self,
        categories: List[str] = None,
        data_api_version: str = None,
        flow_id: str = None,
        flow_name: str = None,
        jsonversion: str = None,
        preview_url: str = None,
        preview_url_expires: int = None,
        status: str = None,
    ):
        # The categories of the Flow.
        self.categories = categories
        # The version number of the API.
        self.data_api_version = data_api_version
        # The Flow ID.
        self.flow_id = flow_id
        # The Flow name.
        self.flow_name = flow_name
        # The JSON version.
        self.jsonversion = jsonversion
        # The temporary preview URL.
        self.preview_url = preview_url
        # The time when the preview URL expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.preview_url_expires = preview_url_expires
        # The state of the Flow.
        # 
        # Valid values:
        # 
        # *   PUBLISHED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DRAFT
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DEPRECATED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories is not None:
            result['Categories'] = self.categories

        if self.data_api_version is not None:
            result['DataApiVersion'] = self.data_api_version

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.jsonversion is not None:
            result['JSONVersion'] = self.jsonversion

        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url

        if self.preview_url_expires is not None:
            result['PreviewUrlExpires'] = self.preview_url_expires

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        if m.get('DataApiVersion') is not None:
            self.data_api_version = m.get('DataApiVersion')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('JSONVersion') is not None:
            self.jsonversion = m.get('JSONVersion')

        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')

        if m.get('PreviewUrlExpires') is not None:
            self.preview_url_expires = m.get('PreviewUrlExpires')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

