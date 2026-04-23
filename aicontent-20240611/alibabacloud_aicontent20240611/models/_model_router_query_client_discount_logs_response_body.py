# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ModelRouterQueryClientDiscountLogsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ModelRouterQueryClientDiscountLogsResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        # maxResults
        self.max_results = max_results
        # nextToken
        self.next_token = next_token
        self.request_id = request_id
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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ModelRouterQueryClientDiscountLogsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ModelRouterQueryClientDiscountLogsResponseBodyData(DaraModel):
    def __init__(
        self,
        client_id: int = None,
        delete_tag: int = None,
        discount: float = None,
        effective_time: str = None,
        expire_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remark: str = None,
    ):
        self.client_id = client_id
        self.delete_tag = delete_tag
        self.discount = discount
        self.effective_time = effective_time
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.delete_tag is not None:
            result['deleteTag'] = self.delete_tag

        if self.discount is not None:
            result['discount'] = self.discount

        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('deleteTag') is not None:
            self.delete_tag = m.get('deleteTag')

        if m.get('discount') is not None:
            self.discount = m.get('discount')

        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

