# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadVerifyRecordIntlRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        code: str = None,
        download_mode: str = None,
        param: str = None,
        product_type: str = None,
    ):
        # Business type:
        # - INVOKE_STATISTICS
        # - INVOKE_RECORD
        self.biz_type = biz_type
        # Query code.
        self.code = code
        # Download mode:
        # 
        # - **async**: Asynchronous
        # - **sync**: Synchronous
        self.download_mode = download_mode
        # Parameters related to the export and download query task.
        self.param = param
        # Product Code.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.code is not None:
            result['Code'] = self.code

        if self.download_mode is not None:
            result['DownloadMode'] = self.download_mode

        if self.param is not None:
            result['Param'] = self.param

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DownloadMode') is not None:
            self.download_mode = m.get('DownloadMode')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

