# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserUploadFileJobRequest(DaraModel):
    def __init__(
        self,
        job_key: str = None,
        tid: int = None,
    ):
        # The key of the file upload task. The key is returned when you call the [CreateUploadFileJob](https://help.aliyun.com/document_detail/206059.html) or [CreateUploadOSSFileJob](https://help.aliyun.com/document_detail/206060.html) operation.
        # 
        # This parameter is required.
        self.job_key = job_key
        # The tenant ID.
        # 
        # > To view the tenant ID, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_key is not None:
            result['JobKey'] = self.job_key

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

