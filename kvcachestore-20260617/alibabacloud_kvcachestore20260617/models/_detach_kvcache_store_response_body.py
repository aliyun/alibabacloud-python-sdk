# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kvcachestore20260617 import models as main_models
from darabonba.model import DaraModel

class DetachKVCacheStoreResponseBody(DaraModel):
    def __init__(
        self,
        detach_results: List[main_models.DetachKVCacheStoreResponseBodyDetachResults] = None,
        request_id: str = None,
    ):
        # The list of unmount results.
        self.detach_results = detach_results
        # The request ID. A request ID is returned regardless of whether the API call succeeds.
        self.request_id = request_id

    def validate(self):
        if self.detach_results:
            for v1 in self.detach_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DetachResults'] = []
        if self.detach_results is not None:
            for k1 in self.detach_results:
                result['DetachResults'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detach_results = []
        if m.get('DetachResults') is not None:
            for k1 in m.get('DetachResults'):
                temp_model = main_models.DetachKVCacheStoreResponseBodyDetachResults()
                self.detach_results.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DetachKVCacheStoreResponseBodyDetachResults(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        kvcs_id: str = None,
        status: str = None,
        vsc_id: str = None,
    ):
        # The error code when the operation fails. This value is null when the operation succeeds.
        self.error_code = error_code
        # The error message when the operation fails. This value is null when the operation succeeds.
        self.error_message = error_message
        # KVCacheStore KvcsId
        self.kvcs_id = kvcs_id
        # The operation result. Valid values:
        # 
        # - DETACHING: The request has been accepted and the asynchronous unmount is in progress. This value is also returned for idempotent calls.
        # - Success: The synchronous validation passed and the asynchronous operation completed.
        # - Failed: The operation failed.
        self.status = status
        # The VSC ID on the compute side.
        self.vsc_id = vsc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.kvcs_id is not None:
            result['KvcsId'] = self.kvcs_id

        if self.status is not None:
            result['Status'] = self.status

        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('KvcsId') is not None:
            self.kvcs_id = m.get('KvcsId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')

        return self

